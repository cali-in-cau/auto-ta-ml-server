from fastbook import *
from kornia import rgb_to_grayscale

class RGB2GreyTransform(DisplayedTransform):
    order = 15 # run after IntToFloatTransform
    def encodes(self, o:TensorImage):
        c = o.shape[1]
        return rgb_to_grayscale(o).expand(-1,c,-1,-1)

def prediction_model_image_deep():
    prediction_dict = {}
    data = './RICKSHAWMAN_BULL_SAMPLE.png'
    path = Path()
    #빈도가 가장 높은 상위 29개의 대한 class에 대한 예측
    learn_inf = load_learner(path/'prediction_model.pkl')
    predict_list = learn_inf.predict(data)[2]
    predict_category = learn_inf.dls.vocab
    '''
    ['CDL3OUTSIDE_BEAR', 'CDL3OUTSIDE_BULL', 'CDLBELTHOLD_BEAR', 'CDLBELTHOLD_BULL', 'CDLCLOSINGMARUBOZU_BEAR', 'CDLCLOSINGMARUBOZU_BULL',
    'CDLDOJI_BULL', 'CDLENGULFING_BEAR', 'CDLENGULFING_BULL', 'CDLHAMMER_BULL', 'CDLHANGINGMAN_BEAR', 'CDLHARAMI_BEAR', 'CDLHARAMI_BULL', 
    'CDLHIGHWAVE_BEAR', 'CDLHIGHWAVE_BULL', 'CDLHIKKAKE_BEAR', 'CDLHIKKAKE_BULL', 'CDLLONGLEGGEDDOJI_BULL', 'CDLLONGLINE_BEAR', 
    'CDLLONGLINE_BULL', 'CDLMARUBOZU_BEAR', 'CDLMARUBOZU_BULL', 'CDLMATCHINGLOW_BULL', 'CDLRICKSHAWMAN_BULL', 'CDLSHOOTINGSTAR_BEAR', 
    'CDLSHORTLINE_BEAR', 'CDLSHORTLINE_BULL', 'CDLSPINNINGTOP_BEAR', 'CDLSPINNINGTOP_BULL']
    '''
    for i, v in enumerate(predict_category):
        prediction_dict[v] = float(predict_list[i])
    
    prediction_dict = sorted(prediction_dict.items(), key=lambda x: x[1], reverse=True)
    print(prediction_dict)
    return prediction_dict

def prediction_model_lstm_gan_deep():
    pass


prediction_model_image_deep()

