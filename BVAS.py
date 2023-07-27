import streamlit as st
st.set_page_config(layout="wide")
st.title("Birmingham Vasculitis Activity Score (BVAS)")

st.title('1, 全身症状')
st.subheader('筋肉痛')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option1s = st.radio('持続', options, key="1")
with col2:
    options = ['無 (0)','有 (1)']
    selected_option1o= st.radio('新規/増悪',options, key="2")    
st.subheader('関節痛/関節炎')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option2s = st.radio('持続', options, key="3")
with col2:
    options = ['無 (0)','有 (1)']
    selected_option2o= st.radio('新規/増悪',options, key="4")    
st.subheader('発熱（38.0度以上）')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option3s = st.radio('持続', options, key="5")
with col2:
    options = ['無 (0)','有 (2)']
    selected_option3o= st.radio('新規/増悪',options, key="6")   
st.subheader('体重減少（2 kg以上）')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option4s = st.radio('持続', options, key="7")
with col2:
    options = ['無 (0)','有 (2)']
    selected_option4o= st.radio('新規/増悪',options, key="8")

#1の点数
scores1s=int(selected_option1s[-2])+int(selected_option2s[-2])+int(selected_option3s[-2])+\
    int(selected_option4s[-2])
if scores1s>2:
    scores1s=2
else:
    scores1s=scores1s
scores1o=int(selected_option1o[-2])+int(selected_option2o[-2])+int(selected_option3o[-2])+\
    int(selected_option4o[-2])
if scores1o>3:
    scores1o=3
else:
    scores1o=scores1o
col1, col2 = st.columns((1,1))
with col1:
    st.write('1, 持続 スコア:',str(scores1s)+"/2")
with col2:
    st.write('1, 新規/増悪 スコア:',str(scores1o)+"/3")
    
st.title('2, 皮膚病変')
st.subheader('梗塞')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option5s = st.radio('持続', options, key="9")
with col2:
    options = ['無 (0)','有 (2)']
    selected_option5o= st.radio('新規/増悪',options, key="10")
st.subheader('紫斑')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option6s = st.radio('持続', options, key="11")
with col2:
    options = ['無 (0)','有 (2)']
    selected_option6o= st.radio('新規/増悪',options, key="12")
st.subheader('潰瘍')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option7s = st.radio('持続', options, key="13")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option7o= st.radio('新規/増悪',options, key="14")
st.subheader('壊疽')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option8s = st.radio('持続', options, key="15")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option8o= st.radio('新規/増悪',options, key="16")
st.subheader('他の皮膚血管炎')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option9s = st.radio('持続', options, key="17")
with col2:
    options = ['無 (0)','有 (2)']
    selected_option9o= st.radio('新規/増悪',options, key="18")
    
#2の点数
scores2s=int(selected_option5s[-2])+int(selected_option6s[-2])+int(selected_option7s[-2])+\
    int(selected_option8s[-2])+int(selected_option9s[-2])
if scores2s>3:
    scores2s=3
else:
    scores2s=scores2s 
scores2o=int(selected_option5o[-2])+int(selected_option6o[-2])+int(selected_option7o[-2])+\
    int(selected_option8o[-2])+int(selected_option9o[-2])
if scores2o>6: 
    scores2o=6
else:
    scores2o=scores2o
col1, col2 = st.columns((1,1))
with col1:
    st.write('2, 持続 スコア:',str(scores2s)+"/3")
with col2:
    st.write('2, 新規/増悪 スコア:',str(scores2o)+"/6")  

st.title('3, 粘膜/眼病変')
st.subheader('口腔潰瘍/口腔内肉芽腫')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option10s = st.radio('持続', options, key="19")
with col2:
    options = ['無 (0)','有 (2)']
    selected_option10o= st.radio('新規/増悪',options, key="20")
st.subheader('陰部潰瘍')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option11s = st.radio('持続', options, key="21")
with col2:
    options = ['無 (0)','有 (1)']
    selected_option11o= st.radio('新規/増悪',options, key="22")
st.subheader('唾液腺炎あるいは涙腺炎')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option12s = st.radio('持続', options, key="23")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option12o= st.radio('新規/増悪',options, key="24")
st.subheader('眼球突出')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option13s = st.radio('持続', options, key="25")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option13o= st.radio('新規/増悪',options, key="26")
st.subheader('上/強膜炎')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option14s = st.radio('持続', options, key="27")
with col2:
    options = ['無 (0)','有 (2)']
    selected_option14o= st.radio('新規/増悪',options, key="28")
st.subheader('結膜炎/眼瞼炎/角膜炎')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option15s = st.radio('持続', options, key="29")
with col2:
    options = ['無 (0)','有 (1)']
    selected_option15o= st.radio('新規/増悪',options, key="30")
st.subheader('霧視')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option16s = st.radio('持続', options, key="31")
with col2:
    options = ['無 (0)','有 (3)']
    selected_option16o= st.radio('新規/増悪',options, key="32")
st.subheader('突然の失明')
col1, col2 = st.columns((1,1))
with col1:
    options = ['(0)']
    selected_option17s = st.radio('持続', options, key="33")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option17o= st.radio('新規/増悪',options, key="34")
st.subheader('ブドウ膜炎')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option18s = st.radio('持続', options, key="35")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option18o= st.radio('新規/増悪',options, key="36")
st.subheader('網膜変化（血管炎/血栓症/滲出物/出血）')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option19s = st.radio('持続', options, key="37")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option19o= st.radio('新規/増悪',options, key="38")
    
#3の点数
scores3s=int(selected_option10s[-2])+int(selected_option11s[-2])+int(selected_option12s[-2])+\
    int(selected_option13s[-2])+int(selected_option14s[-2])+int(selected_option15s[-2])+\
    int(selected_option16s[-2])+int(selected_option17s[-2])+int(selected_option18s[-2])+\
    int(selected_option19s[-2])
if scores3s>3:
    scores3s=3
else:
    scores3s=scores3s
scores3o=int(selected_option10o[-2])+int(selected_option11o[-2])+int(selected_option12o[-2])+\
    int(selected_option13o[-2])+int(selected_option14o[-2])+int(selected_option15o[-2])+\
    int(selected_option16o[-2])+int(selected_option17o[-2])+int(selected_option18o[-2])+\
    int(selected_option19o[-2])
if scores3o>6:
    scores3o=6
else:
    scores3o=scores3o
col1, col2 = st.columns((1,1))
with col1:
    st.write('3, 持続 スコア:',str(scores3s)+"/3")
with col2:
    st.write('3, 新規/増悪 スコア:',str(scores3o)+"/6")
    
st.title('4, 耳・鼻・咽喉病変')
st.subheader('鼻出血/痂皮形成、鼻腔内潰瘍/肉芽腫')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option20s = st.radio('持続', options, key="39")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option20o= st.radio('新規/増悪',options, key="40")
st.subheader('副鼻腔病変')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option21s = st.radio('持続', options, key="41")
with col2:
    options = ['無 (0)','有 (2)']
    selected_option21o= st.radio('新規/増悪',options, key="42")
st.subheader('声門下狭窄')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (3)']
    selected_option22s = st.radio('持続', options, key="43")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option22o= st.radio('新規/増悪',options, key="44")
st.subheader('伝音性難聴')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option23s = st.radio('持続', options, key="45")
with col2:
    options = ['無 (0)','有 (3)']
    selected_option23o= st.radio('新規/増悪',options, key="46")
st.subheader('感音性難聴')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option24s = st.radio('持続', options, key="47")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option24o= st.radio('新規/増悪',options, key="48")
#4の点数
scores4s=int(selected_option20s[-2])+int(selected_option21s[-2])+int(selected_option22s[-2])+\
    int(selected_option23s[-2])+int(selected_option24s[-2])
if scores4s>3:
    scores4s=3
else:
    scores4s=scores4s
scores4o=int(selected_option20o[-2])+int(selected_option21o[-2])+int(selected_option22o[-2])+\
    int(selected_option23o[-2])+int(selected_option24o[-2])
if scores4o>6:
    scores4o=6
else:
    scores4o=scores4o
col1, col2 = st.columns((1,1))
with col1:
    st.write('4, 持続 スコア:',str(scores4s)+"/3")
with col2:
    st.write('4, 新規/増悪 スコア:',str(scores4o)+"/6")

st.title('5, 胸部')
st.subheader('喘鳴')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option25s = st.radio('持続', options, key="49")
with col2:
    options = ['無 (0)','有 (2)']
    selected_option25o= st.radio('新規/増悪',options, key="50")
st.subheader('結節または空洞')
col1, col2 = st.columns((1,1))
with col1:
    options = ['(0)']
    selected_option26s = st.radio('持続', options, key="51")
with col2:
    options = ['無 (0)','有 (3)']
    selected_option26o= st.radio('新規/増悪',options, key="52")
st.subheader('胸水/胸膜炎')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option27s = st.radio('持続', options, key="53")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option27o= st.radio('新規/増悪',options, key="54")
st.subheader('浸潤影')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option28s = st.radio('持続', options, key="55")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option28o= st.radio('新規/増悪',options, key="56")
st.subheader('気管内の偽腫瘍/潰瘍病変')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option29s = st.radio('持続', options, key="57")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option29o= st.radio('新規/増悪',options, key="58")
st.subheader('大量喀血/肺胞出血')
col1, col2 = st.columns((1,1))
with col1:
    options=['無 (0)','有 (4)']
    selected_option30s = st.radio('持続', options, key="59")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option30o= st.radio('新規/増悪',options, key="60")
st.subheader('呼吸不全')
col1, col2 = st.columns((1,1))
with col1:
    options=['無 (0)','有 (4)']
    selected_option31s = st.radio('持続', options, key="61")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option31o= st.radio('新規/増悪',options, key="62")
#5の点数
scores5s=int(selected_option25s[-2])+int(selected_option26s[-2])+int(selected_option27s[-2])+\
    int(selected_option28s[-2])+int(selected_option29s[-2])+int(selected_option30s[-2])+\
    int(selected_option31s[-2])
if scores5s>3:
    scores5s=3
else:
    scores5s=scores5s
scores5o=int(selected_option25o[-2])+int(selected_option26o[-2])+int(selected_option27o[-2])+\
    int(selected_option28o[-2])+int(selected_option29o[-2])+int(selected_option30o[-2])+\
    int(selected_option31o[-2])
if scores5o>6:
    scores5o=6
else:
    scores5o=scores5o
col1, col2 = st.columns((1,1))
with col1:
    st.write('5, 持続 スコア:',str(scores5s)+"/3")
with col2:
    st.write('5, 新規/増悪 スコア:',str(scores5o)+"/6")

st.title('6, 心血管病変')
st.subheader('脈拍消失')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option32s = st.radio('持続', options, key="63")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option32o= st.radio('新規/増悪',options, key="64")
st.subheader('心弁膜症')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option33s = st.radio('持続', options, key="65")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option33o= st.radio('新規/増悪',options, key="66")
st.subheader('心外膜炎')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option34s = st.radio('持続', options, key="67")
with col2:
    options = ['無 (0)','有 (3)']
    selected_option34o= st.radio('新規/増悪',options, key="68")
st.subheader('狭心痛')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option35s = st.radio('持続', options, key="69")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option35o= st.radio('新規/増悪',options, key="70")
st.subheader('心筋症')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (3)']
    selected_option36s = st.radio('持続', options, key="71")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option36o= st.radio('新規/増悪',options, key="72")
st.subheader('うっ血性心不全')
col1, col2 = st.columns((1,1))
with col1:
    options=['無 (0)','有 (3)']
    selected_option37s = st.radio('持続', options, key="73")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option37o= st.radio('新規/増悪',options, key="74")
#6の点数
scores6s=int(selected_option32s[-2])+int(selected_option33s[-2])+int(selected_option34s[-2])+\
    int(selected_option35s[-2])+int(selected_option36s[-2])+int(selected_option37s[-2])
if scores6s>3:
    scores6s=3
else:
    scores6s=scores6s
scores6o=int(selected_option32o[-2])+int(selected_option33o[-2])+int(selected_option34o[-2])+\
    int(selected_option35o[-2])+int(selected_option36o[-2])+int(selected_option37o[-2])
if scores6o>6:
    scores6o=6
else:
    scores6o=scores6o
col1, col2 = st.columns((1,1))
with col1:
    st.write('6, 持続 スコア:',str(scores6s)+"/3")
with col2:
    st.write('6, 新規/増悪 スコア:',str(scores6o)+"/6")

st.title('7, 腹部')
st.subheader('腹膜炎')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (3)']
    selected_option38s = st.radio('持続', options, key="75")
with col2:
    options = ['無 (0)','有 (9)']
    selected_option38o= st.radio('新規/増悪',options, key="76")
st.subheader('血性下痢')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (3)']
    selected_option39s = st.radio('持続', options, key="77")
with col2:
    options = ['無 (0)','有 (9)']
    selected_option39o= st.radio('新規/増悪',options, key="78")
st.subheader('虚血による腹痛')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option40s = st.radio('持続', options, key="79")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option40o= st.radio('新規/増悪',options, key="80")

#7の点数
scores7s=int(selected_option38s[-2])+int(selected_option39s[-2])+int(selected_option40s[-2])
if scores7s>4:
    scores7s=4
else:
    scores7s=scores7s
scores7o=int(selected_option38o[-2])+int(selected_option39o[-2])+int(selected_option40o[-2])
if scores7o>9:
    scores7o=9
else:
    scores7o=scores7o
col1, col2 = st.columns((1,1))
with col1:
    st.write('7, 持続 スコア:',str(scores7s)+"/4")
with col2:
    st.write('7, 新規/増悪 スコア:',str(scores7o)+"/9")

st.title('8, 腎病変')
st.subheader('高血圧（拡張期血圧>95 mmHg）')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option41s = st.radio('持続', options, key="81")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option41o= st.radio('新規/増悪',options, key="82")
st.subheader('蛋白尿（>1+あるいは>0.2 g/日）')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option42s = st.radio('持続', options, key="83")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option42o= st.radio('新規/増悪',options, key="84")
st.subheader('血尿（>1+あるいは>10 RBC/hpf）')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (3)']
    selected_option43s = st.radio('持続', options, key="85")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option43o= st.radio('新規/増悪',options, key="86")
st.subheader('血清クレアチニン値1.4-2.79 mg/dL')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (2)']
    selected_option44s = st.radio('持続', options, key="87")
with col2:
    options = ['無 (0)','有 (4)']
    selected_option44o= st.radio('新規/増悪',options, key="88")
st.subheader('血清クレアチニン値2.8-5.69 mg/dL')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (3)']
    selected_option45s = st.radio('持続', options, key="89")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option45o= st.radio('新規/増悪',options, key="90")
st.subheader('血清クレアチニン値≧5.7 mg/dL')
col1, col2 = st.columns((1,1))
with col1:
    options=['無 (0)','有 (4)']
    selected_option46s = st.radio('持続', options, key="91")
with col2:
    options = ['無 (0)','有 (8)']
    selected_option46o= st.radio('新規/増悪',options, key="92")
st.subheader('血清クレアチニン値増加>30%あるいはクレアチニンクリアランス低下>25%')
col1, col2 = st.columns((1,1))
with col1:
    options=['(0)']
    selected_option47s = st.radio('持続', options, key="93")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option47o= st.radio('新規/増悪',options, key="94")
    
#8の点数
scores8s=int(selected_option41s[-2])+int(selected_option42s[-2])+int(selected_option43s[-2])+\
    int(selected_option44s[-2])+int(selected_option45s[-2])+int(selected_option46s[-2])+\
    int(selected_option47s[-2])
if scores8s>6:
    scores8s=6
else:
    scores8s=scores8s
scores8o=int(selected_option41o[-2])+int(selected_option42o[-2])+int(selected_option43o[-2])+\
    int(selected_option44o[-2])+int(selected_option45o[-2])+int(selected_option46o[-2])+\
    int(selected_option47o[-2])
if scores8o>12:
    scores8o=12
else:
    scores8o=scores8o
col1, col2 = st.columns((1,1))
with col1:
    st.write('8, 持続 スコア:',str(scores8s)+"/6")
with col2:
    st.write('8, 新規/増悪 スコア:',str(scores8o)+"/12")

st.title('9, 神経系病変')
st.subheader('頭痛')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option48s = st.radio('持続', options, key="95")
with col2:
    options = ['無 (0)','有 (1)']
    selected_option48o= st.radio('新規/増悪',options, key="96")
st.subheader('髄膜炎')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option49s = st.radio('持続', options, key="97")
with col2:
    options = ['無 (0)','有 (3)']
    selected_option49o= st.radio('新規/増悪',options, key="98")
st.subheader('器質性錯乱')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (1)']
    selected_option50s = st.radio('持続', options, key="99")
with col2:
    options = ['無 (0)','有 (3)']
    selected_option50o= st.radio('新規/増悪',options, key="100")
st.subheader('痙攣（高血圧性でない）')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (3)']
    selected_option51s = st.radio('持続', options, key="101")
with col2:
    options = ['無 (0)','有 (9)']
    selected_option51o= st.radio('新規/増悪',options, key="102")
st.subheader('脳卒中')
col1, col2 = st.columns((1,1))
with col1:
    options = ['無 (0)','有 (3)']
    selected_option52s = st.radio('持続', options, key="103")
with col2:
    options = ['無 (0)','有 (9)']
    selected_option52o= st.radio('新規/増悪',options, key="104")
st.subheader('脊髄病変')
col1, col2 = st.columns((1,1))
with col1:
    options=['無 (0)','有 (3)']
    selected_option53s = st.radio('持続', options, key="105")
with col2:
    options = ['無 (0)','有 (9)']
    selected_option53o= st.radio('新規/増悪',options, key="106")
st.subheader('脳神経麻痺')
col1, col2 = st.columns((1,1))
with col1:
    options=['無 (0)','有 (3)']
    selected_option54s = st.radio('持続', options, key="107")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option54o= st.radio('新規/増悪',options, key="108")
st.subheader('感覚性末梢神経障害')
col1, col2 = st.columns((1,1))
with col1:
    options=['無 (0)','有 (3)']
    selected_option55s = st.radio('持続', options, key="109")
with col2:
    options = ['無 (0)','有 (6)']
    selected_option55o= st.radio('新規/増悪',options, key="110")
st.subheader('運動性多発性単神経炎')
col1, col2 = st.columns((1,1))
with col1:
    options=['無 (0)','有 (3)']
    selected_option56s = st.radio('持続', options, key="111")
with col2:
    options = ['無 (0)','有 (9)']
    selected_option56o= st.radio('新規/増悪',options, key="112")    

#9の点数
scores9s=int(selected_option48s[-2])+int(selected_option49s[-2])+int(selected_option50s[-2])+\
    int(selected_option51s[-2])+int(selected_option52s[-2])+int(selected_option53s[-2])+\
    int(selected_option54s[-2])+int(selected_option55s[-2])+int(selected_option56s[-2])
if scores9s>6:
    scores9s=6
else:
    scores9s=scores9s
scores9o=int(selected_option48o[-2])+int(selected_option49o[-2])+int(selected_option50o[-2])+\
    int(selected_option51o[-2])+int(selected_option52o[-2])+int(selected_option53o[-2])+\
    int(selected_option54o[-2])+int(selected_option55o[-2])+int(selected_option56o[-2])
if scores9o>9:
    scores9o=9
else:
    scores9o=scores9o
col1, col2 = st.columns((1,1))
with col1:
    st.write('9, 持続 スコア:',str(scores9s)+"/6")
with col2:
    st.write('9, 新規/増悪 スコア:',str(scores9o)+"/9")
    

st.title('合計')
col1, col2 = st.columns((1,1))
with col1:
    scores=scores1s+scores2s+scores3s+scores4s+scores5s+scores6s+scores7s+scores8s+scores9s
    st.write('持続 スコア:',str(scores)+"/33")
with col2:
    scoreso=scores1o+scores2o+scores3o+scores4o+scores5o+scores6o+scores7o+scores8o+scores9o
    st.write('新規/増悪 スコア:',str(scoreso)+"/63")