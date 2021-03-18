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

if upload_file is None:
    st.write('Please upload a dataset')

elif upload_file is not None:
    upload_file.seek(0)

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

    df_prio1_AZ = df.loc[(df['PRIORITY'] == 'Priority 1')
                        & (df['VACCINE'] == 'ASTRAZENECA')
                        & (df['STATUS'] == 1), :]

    df_prio1_SV = df.loc[(df['PRIORITY'] == 'Priority 1')
                         & (df['VACCINE'] == 'SINOVAC')
                         & (df['STATUS'] == 1), :]

    df_prio2_AZ = df.loc[(df['PRIORITY'] == 'Priority 2')
                         & (df['VACCINE'] == 'ASTRAZENECA')
                         & (df['STATUS'] == 1), :]

    df_prio2_SV = df.loc[(df['PRIORITY'] == 'Priority 2')
                        & (df['VACCINE'] == 'SINOVAC')
                        & (df['STATUS'] == 1), :]

    df_prio3_AZ = df.loc[(df['PRIORITY'] == 'Priority 3')
                         & (df['VACCINE'] == 'ASTRAZENECA')
                         & (df['STATUS'] == 1), :]

    df_prio3_SV = df.loc[(df['PRIORITY'] == 'Priority 3')
                         & (df['VACCINE'] == 'SINOVAC')
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

    prio1_AZ_count = df_prio1_AZ.PRIORITY.count()
    prio1_SV_count = df_prio1_SV.PRIORITY.count()
    prio1_all_count = prio1_AZ_count + prio1_SV_count

    prio2_AZ_count = df_prio2_AZ.PRIORITY.count()
    prio2_SV_count = df_prio2_SV.PRIORITY.count()
    prio2_all_count = prio2_AZ_count + prio2_SV_count

    prio3_AZ_count = df_prio3_AZ.PRIORITY.count()
    prio3_SV_count = df_prio3_SV.PRIORITY.count()
    prio3_all_count = prio3_AZ_count + prio3_SV_count


    st.markdown('# **Vaccination Figures:**')

    # vaccinated
    st.markdown('## **Vaccinated:** {}'.format(vax_count))
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(az_count))
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(sino_count))

    # priority group
    st.markdown('## **All Vaccinated as to Priority Group:**')
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 1:** {}'.format(prio1_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(prio1_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(prio1_SV_count))

    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 2:** {}'.format(prio2_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(prio2_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(prio2_SV_count))

    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 3:** {}'.format(prio3_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(prio3_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(prio3_SV_count))

    # AEFI
    st.markdown('## **With Reported AEFI:** {}'.format(aefi_count))
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp; **Mild:** {}'.format(aefi_mild_count))
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp; **Severe:** {}'.format(aefi_sev_count))

    # deferred
    st.markdown('## **Deferred:** {}'.format(def_count))

    st.markdown('##')


    #st.dataframe(df)
