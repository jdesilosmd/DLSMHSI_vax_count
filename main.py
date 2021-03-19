import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import datetime as dt
from datetime import date
today = dt.date.today()


#############################
# HEADER AND SIDEBAR
#############################

st.title('DLSMHSI Vaccination Data Tracker')

st.sidebar.markdown('#### Today is {}.'.format(today))
st.sidebar.markdown('#### Download the latest [COVID-19 Data](https://www.doh.gov.ph/covid19tracker) from the DOH Data Drop')
st.sidebar.markdown('#### DOH Data Drop dataset can also be accessed [here](https://drive.google.com/drive/folders/1ZPPcVU4M7T-dtRyUceb0pMAd8ickYf8o).')


#############################
# DATA UPLOAD
#############################

# Upload data here:
upload_file = st.file_uploader('Upload data here: ',
                               type=['xlsx', 'xls'])

if upload_file is None:
    st.write('Please upload a dataset')

elif upload_file is not None:
    upload_file.seek(0)

    df = pd.read_excel(upload_file)


#############################
# DATA PROCESSING
#############################

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

# Priority Group - Vaccinated

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



# Priority group - severe AEFI

## Priority 1
    df_mild1_AZ = df.loc[(df['PRIORITY'] == 'Priority 1')
                        & (df['VACCINE'] == 'ASTRAZENECA')
                        & (df['AEFI'] == 2), :]

    df_mild1_SV = df.loc[(df['PRIORITY'] == 'Priority 1')
                        & (df['VACCINE'] == 'SINOVAC')
                        & (df['AEFI'] == 2), :]

## Priority 2
    df_mild2_AZ = df.loc[(df['PRIORITY'] == 'Priority 2')
                         & (df['VACCINE'] == 'ASTRAZENECA')
                         & (df['AEFI'] == 2), :]

    df_mild2_SV = df.loc[(df['PRIORITY'] == 'Priority 2')
                         & (df['VACCINE'] == 'SINOVAC')
                         & (df['AEFI'] == 2), :]

## Priority 3
    df_mild3_AZ = df.loc[(df['PRIORITY'] == 'Priority 3')
                         & (df['VACCINE'] == 'ASTRAZENECA')
                         & (df['AEFI'] == 2), :]

    df_mild3_SV = df.loc[(df['PRIORITY'] == 'Priority 3')
                         & (df['VACCINE'] == 'SINOVAC')
                         & (df['AEFI'] == 2), :]

# Priority group - severe AEFI

## Priority 1
    df_sev1_AZ = df.loc[(df['PRIORITY'] == 'Priority 1')
                         & (df['VACCINE'] == 'ASTRAZENECA')
                         & (df['AEFI'] == 1), :]

    df_sev1_SV = df.loc[(df['PRIORITY'] == 'Priority 1')
                         & (df['VACCINE'] == 'SINOVAC')
                         & (df['AEFI'] == 1), :]

## Priority 2
    df_sev2_AZ = df.loc[(df['PRIORITY'] == 'Priority 2')
                         & (df['VACCINE'] == 'ASTRAZENECA')
                         & (df['AEFI'] == 1), :]

    df_sev2_SV = df.loc[(df['PRIORITY'] == 'Priority 2')
                         & (df['VACCINE'] == 'SINOVAC')
                         & (df['AEFI'] == 1), :]

## Priority 3
    df_sev3_AZ = df.loc[(df['PRIORITY'] == 'Priority 3')
                         & (df['VACCINE'] == 'ASTRAZENECA')
                         & (df['AEFI'] == 1), :]

    df_sev3_SV = df.loc[(df['PRIORITY'] == 'Priority 3')
                         & (df['VACCINE'] == 'SINOVAC')
                         & (df['AEFI'] == 1), :]


    def_count = df_def.STATUS.count()
    az_count = df_az.VACCINE.count()
    sino_count = df_sino.VACCINE.count()
    vax_count = az_count + sino_count
    aefi_mild_count = df_aefi_mild.AEFI.count()
    aefi_sev_count = df_aefi_sev.AEFI.count()
    aefi_count = aefi_mild_count + aefi_sev_count
    unvax_count = df_unvax.STATUS.count()
    out_count = df_outvax.VACCINE.count()

# priority group - Vaccinated
    prio1_AZ_count = df_prio1_AZ.PRIORITY.count()
    prio1_SV_count = df_prio1_SV.PRIORITY.count()
    prio1_all_count = prio1_AZ_count + prio1_SV_count

    prio2_AZ_count = df_prio2_AZ.PRIORITY.count()
    prio2_SV_count = df_prio2_SV.PRIORITY.count()
    prio2_all_count = prio2_AZ_count + prio2_SV_count

    prio3_AZ_count = df_prio3_AZ.PRIORITY.count()
    prio3_SV_count = df_prio3_SV.PRIORITY.count()
    prio3_all_count = prio3_AZ_count + prio3_SV_count

# priority group - AEFI mild
    mild1_AZ_count = df_mild1_AZ.PRIORITY.count()
    mild1_SV_count = df_mild1_SV.PRIORITY.count()
    mild1_all_count = mild1_AZ_count + mild1_SV_count

    mild2_AZ_count = df_mild2_AZ.PRIORITY.count()
    mild2_SV_count = df_mild2_SV.PRIORITY.count()
    mild2_all_count = mild2_AZ_count + mild2_SV_count

    mild3_AZ_count = df_mild3_AZ.PRIORITY.count()
    mild3_SV_count = df_mild3_SV.PRIORITY.count()
    mild3_all_count = mild3_AZ_count + mild3_SV_count

    # priority group - AEFI mild
    sev1_AZ_count = df_sev1_AZ.PRIORITY.count()
    sev1_SV_count = df_sev1_SV.PRIORITY.count()
    sev1_all_count = sev1_AZ_count + sev1_SV_count

    sev2_AZ_count = df_sev2_AZ.PRIORITY.count()
    sev2_SV_count = df_sev2_SV.PRIORITY.count()
    sev2_all_count = sev2_AZ_count + sev2_SV_count

    sev3_AZ_count = df_sev3_AZ.PRIORITY.count()
    sev3_SV_count = df_sev3_SV.PRIORITY.count()
    sev3_all_count = sev3_AZ_count + sev3_SV_count


#############################
# DASHBOARD
#############################

    st.markdown('# **Vaccination Figures:**')

    st.markdown(" ")

# vaccinated
    st.markdown('## **Vaccinated:** {}'.format(vax_count))
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(az_count))
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(sino_count))

### vaccinated graph

    vax_bar = go.Figure()
    vax_bar.add_trace(go.Bar(
        y=['Vaccinated'],
        x=[az_count],
        name='AstraZeneca',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))

    vax_bar.add_trace(go.Bar(
        y=['Vaccinated'],
        x = [sino_count],
        name = 'Sinovac',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    vax_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor = 'white',
        height = 220,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(vax_bar)


    st.markdown(" ")
    st.markdown(" ")

## priority group - vaccinated
    st.markdown('## **All Vaccinated as to Priority Group:**')
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 1:** {}'.format(prio1_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(prio1_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(prio1_SV_count))

    ### Priority vaccinated graph

    # Priority 1
    prio1_vax_bar = go.Figure()
    prio1_vax_bar.add_trace(go.Bar(
        y=['Priority 1'],
        x=[prio1_AZ_count],
        name='AstraZeneca',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))
    prio1_vax_bar.add_trace(go.Bar(
        y=['Priority 1'],
        x=[prio1_SV_count],
        name='Sinovac',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    prio1_vax_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor='white',
        height=200,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(prio1_vax_bar)


    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 2:** {}'.format(prio2_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(prio2_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(prio2_SV_count))

    # Priority 2
    prio2_vax_bar = go.Figure()
    prio2_vax_bar.add_trace(go.Bar(
        y=['Priority 2'],
        x=[prio2_AZ_count],
        name='AstraZeneca',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))

    prio2_vax_bar.add_trace(go.Bar(
        y=['Priority 2'],
        x=[prio2_SV_count],
        name='Sinovac',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    prio2_vax_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor='white',
        height=200,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(prio2_vax_bar)


    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 3:** {}'.format(prio3_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(prio3_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(prio3_SV_count))

    #Priority 3
    prio3_vax_bar = go.Figure()
    prio3_vax_bar.add_trace(go.Bar(
        y=['Priority 3'],
        x=[prio3_AZ_count],
        name='AstraZeneca',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))

    prio3_vax_bar.add_trace(go.Bar(
        y=['Priority 3'],
        x=[prio3_SV_count],
        name='Sinovac',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    prio3_vax_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor='white',
        height=200,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(prio3_vax_bar)

    st.markdown(" ")
    st.markdown(" ")


    # AEFI
    st.markdown('## **With Reported AEFI:** {}'.format(aefi_count))
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp; **Mild:** {}'.format(aefi_mild_count))
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp; **Severe:** {}'.format(aefi_sev_count))

    #AEFI graph
    aefi_bar = go.Figure()
    aefi_bar.add_trace(go.Bar(
        y=['Observed AEFI'],
        x=[aefi_mild_count],
        name='Mild AEFI',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))
    aefi_bar.add_trace(go.Bar(
        y=['Observed AEFI'],
        x=[aefi_sev_count],
        name='Severe AEFI',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    aefi_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor='white',
        height=200,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(aefi_bar)

    st.markdown(" ")
    st.markdown(" ")

# priority group - mild AEFI
    st.markdown('## **Reported Mild AEFI as to Priority Group:**')
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 1:** {}'.format(mild1_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(mild1_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(mild1_SV_count))

    # Priority 1 mild AEFI graph
    mild_p1_bar = go.Figure()
    mild_p1_bar.add_trace(go.Bar(
        y=['Mild AEFI in Priority 1'],
        x=[mild1_AZ_count],
        name='AstraZeneca',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))
    mild_p1_bar.add_trace(go.Bar(
        y=['Mild AEFI in Priority 1'],
        x=[mild1_SV_count],
        name='Sinovac',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    mild_p1_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor='white',
        height=200,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(mild_p1_bar)

    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 2:** {}'.format(mild2_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(mild2_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(mild2_SV_count))

    # Priority 2 mild AEFI graph
    mild_p2_bar = go.Figure()
    mild_p2_bar.add_trace(go.Bar(
        y=['Mild AEFI in Priority 2'],
        x=[mild2_AZ_count],
        name='AstraZeneca',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))
    mild_p2_bar.add_trace(go.Bar(
        y=['Mild AEFI in Priority 2'],
        x=[mild2_SV_count],
        name='Sinovac',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    mild_p2_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor='white',
        height=200,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(mild_p2_bar)

    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 3:** {}'.format(mild3_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(mild3_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(mild3_SV_count))

    # Priority 3 mild AEFI graph
    mild_p3_bar = go.Figure()
    mild_p3_bar.add_trace(go.Bar(
        y=['Mild AEFI in Priority 3'],
        x=[mild3_AZ_count],
        name='AstraZeneca',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))
    mild_p1_bar.add_trace(go.Bar(
        y=['Mild AEFI in Priority 3'],
        x=[mild3_SV_count],
        name='Sinovac',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    mild_p1_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor='white',
        height=200,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(mild_p3_bar)

    st.markdown(" ")
    st.markdown(" ")

# priority group - severe AEFI
    st.markdown('## **Reported Severe AEFI as to Priority Group:**')
    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 1:** {}'.format(sev1_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(sev1_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(sev1_SV_count))

    # Priority 1 severe AEFI graph
    sev_p1_bar = go.Figure()
    sev_p1_bar.add_trace(go.Bar(
        y=['Severe AEFI in Priority 1'],
        x=[sev1_AZ_count],
        name='AstraZeneca',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))
    sev_p1_bar.add_trace(go.Bar(
        y=['Severe AEFI in Priority 1'],
        x=[sev1_SV_count],
        name='Sinovac',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    sev_p1_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor='white',
        height=200,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(sev_p1_bar)

    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 2:** {}'.format(sev2_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(sev2_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(sev2_SV_count))

    # Priority 2 severe AEFI graph
    sev_p2_bar = go.Figure()
    sev_p2_bar.add_trace(go.Bar(
        y=['Severe AEFI in Priority 2'],
        x=[sev2_AZ_count],
        name='AstraZeneca',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))
    sev_p2_bar.add_trace(go.Bar(
        y=['Severe AEFI in Priority 2'],
        x=[sev2_SV_count],
        name='Sinovac',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    sev_p2_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor='white',
        height=200,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(sev_p2_bar)

    st.markdown('### &ensp;&ensp;&ensp;&ensp;&ensp;**Priority 3:** {}'.format(sev3_all_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**AstraZeneca:** {}'.format(sev3_AZ_count))
    st.markdown(
        '### &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Sinovac:** {}'.format(sev3_SV_count))

    # Priority 3 severe AEFI graph
    sev_p3_bar = go.Figure()
    sev_p3_bar.add_trace(go.Bar(
        y=['Severe AEFI in Priority 3'],
        x=[sev3_AZ_count],
        name='AstraZeneca',
        orientation='h',
        width=[0.2],
        marker=dict(color='deepskyblue')
    ))
    sev_p1_bar.add_trace(go.Bar(
        y=['Severe AEFI in Priority 3'],
        x=[sev3_SV_count],
        name='Sinovac',
        orientation='h',
        width=[0.2],
        marker=dict(color='violet')
    ))

    sev_p1_bar.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),

        template='seaborn',
        paper_bgcolor='white',
        height=200,
        margin=dict(l=15, r=10, t=2, b=2),
        barmode='stack')

    st.plotly_chart(sev_p3_bar)

    st.markdown(" ")
    st.markdown(" ")

# deferred
    st.markdown('## **Deferred:** {}'.format(def_count))

    st.markdown('##')


    #st.dataframe(df)
