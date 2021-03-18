import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import datetime as dt
from datetime import date
today = dt.date.today()


st.title('DLSMHSI Vaccination Data Tracker')

st.sidebar.markdown('#### Today is {}.'.format(today))
st.sidebar.markdown('#### Download the latest [COVID-19 Data](https://www.doh.gov.ph/covid19tracker) from the DOH Data Drop')
st.sidebar.markdown('#### DOH Data Drop dataset can also be accessed [here](https://drive.google.com/drive/folders/1ZPPcVU4M7T-dtRyUceb0pMAd8ickYf8o).')


# Upload data here:
upload_file = st.file_uploader('Upload data here: ',
                               type=['xlsx', 'xls'])

if case_upload is None:
  st.write('Please upload a dataset.')

  elif case_upload is not None:
  
  case_upload.seek(0)
  
  df = pd.read_excel(upload_file)
  df['STATUS'] = df['STATUS'].fillna(2)
  df_def = df.loc[df['STATUS'] == 0, :]
  df_vax = df.loc[df['STATUS'] == 1, :]
  df_aefi_mild = df.loc[df['AEFI'] == 1, :]
  df_aefi_sev = df.loc[df['AEFI'] == 2]
  df_unvax = df.loc[df['STATUS'] == 0, :]
  df_outvax = df.loc[df['VACCINE'] == 'OUTSIDE',:]
  df_az = df.loc[(df['VACCINE'] == 'ASTRAZENECA')
                 & (df['STATUS'] == 1), :]
  df_sino = df.loc[(df['VACCINE'] == 'SINOVAC')
                 & (df['STATUS'] == 1), :]

  def_count = df_def.STATUS.count()
  az_count = df_az.VACCINE.count()
  sino_count = df_sino.VACCINE.count()
  vax_count = az_count + sino_count
  aefi_mild_count = df_aefi_mild.AEFI.count()
  aefi_sev_count = df_aefi_sev.AEFI.count()
  aefi_count = aefi_mild_count + aefi_sev_count
  unvax_count = df_unvax.STATUS.count()
  out_count = df_outvax.VACCINE.count()



  st.markdown('# **Vaccination Figures:**')
  st.markdown('## **Vaccinated:** {}'.format(vax_count))
  st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(az_count))
  st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(sino_count))

  st.markdown('## **With Reported AEFI:** {}'.format(aefi_count))
  st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp; **Mild:** {}'.format(aefi_mild_count))
  st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp; **Severe:** {}'.format(aefi_sev_count))

  st.markdown('## **Deferred:** {}'.format(def_count))


  #st.dataframe(df)
