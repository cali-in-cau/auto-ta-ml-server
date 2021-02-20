from fastbook import *
from kornia import rgb_to_grayscale
import mplfinance as mpf
import os
import uuid
'''
class RGB2GreyTransform(DisplayedTransform):
    order = 15 # run after IntToFloatTransform
    def encodes(self, o:TensorImage):
        c = o.shape[1]
        return rgb_to_grayscale(o).expand(-1,c,-1,-1)
'''
def image_preprocessing(pattern_data, pattern_csv):
    #pattern_data for shown pattern
    #pattern csv for get the data of shown_pattern
    uuid_list = []
    whole_data = pattern_data['bull'] + pattern_data['bear']
    path = path = os.path.join(os.getcwd(), 'ml_model/image_db/')
    for data in whole_data:
        #get the timedata
        date = data[1]
        nei_data = pattern_csv.iloc[pattern_csv.index.get_loc(date) - 2 : pattern_csv.index.get_loc(date) + 3]
        #uuid for image name
        name = uuid.uuid4()
        uuid_list.append((date, name))
        #시각과 image 이름을 기억한다.
        #mplplot setting
        mc = mpf.make_marketcolors(up='r',down='b')
        s  = mpf.make_mpf_style(marketcolors=mc)
        savefig = dict(fname=f'{path}/{name}.png',\
        dpi=50,pad_inches=0,bbox_inches='tight')
        #plot
        mpf.plot(nei_data, axisoff=True, type='candle', style=s, savefig=savefig)
    
    return uuid_list

def predict_model_image_deep(pattern_data, pattern_csv):
    #make the image to image classification
    image_list = image_preprocessing(pattern_data, pattern_csv)
    #get the pkl file
    pkl_path = os.path.join(os.getcwd(), 'ml_model/predict-21-classes.pkl')
    predict_model_image = {}

    #빈도가 가장 높은 상위 21개의 대한 class에 대한 예측
    '''
    ['CDLENGULFING_BULL', 'CDLENGULFING_BEAR', 'CDLSHORTLINE_BULL', 'CDLSHORTLINE_BEAR', 'CDLHIKKAKE_BULL', 'CDLHARAMI_BULL', 'CDLBELTHOLD_BULL', 'CDLHIKKAKE_BEAR', 'CDLHARAMI_BEAR', 'CDLBELTHOLD_BEAR', 'CDLLONGLINE_BULL', 'CDLLONGLINE_BEAR', 'CDLCLOSINGMARUBOZU_BULL', 'CDLHIGHWAVE_BEAR', 'CDLCLOSINGMARUBOZU_BEAR', 'CDLDOJI_BULL', 'CDLRICKSHAWMAN_BULL', 'CDLSPINNINGTOP_BULL', 'CDLHIGHWAVE_BULL', 'CDLSPINNINGTOP_BEAR', 'CDLLONGLEGGEDDOJI_BULL']
    '''
    for image in image_list:
        prediction_dict = {}
        date, real_image = image
        image_data = os.path.join(os.getcwd(), f'ml_model/image_db/{real_image}.png')
        learn_inf = load_learner(pkl_path)
        predict_list = learn_inf.predict(image_data)[2]
        predict_category = learn_inf.dls.vocab
   
        for i, v in enumerate(predict_category):
            prediction_dict[v] = float(predict_list[i])
        
        prediction_dict = sorted(prediction_dict.items(), key=lambda x: x[1], reverse=True)
        predict_model_image[date] = prediction_dict

    return predict_model_image



