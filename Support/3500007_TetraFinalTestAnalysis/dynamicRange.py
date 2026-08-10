import mysql.connector
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from datetime import date


def cal_adc_dfbs(txdf,rxdf,sn):

    Tx_Pout_df = txdf.copy()
    selected_cols = ['RF_FREQ_OUT','p_out_fsl_dBm_',"TX_PORT"]
    Tx_Pout_df = Tx_Pout_df[selected_cols]

    Rx_gain_df = rxdf.copy()
    selected_cols = ['RF_FREQ','peak_gain_dB_',"RX_PORT"]
    Rx_gain_df = Rx_gain_df[selected_cols]

    Tx_Pout_df = Tx_Pout_df[(Tx_Pout_df['RF_FREQ_OUT']>=21.0) & (Tx_Pout_df['RF_FREQ_OUT']<=38.0)]
    Rx_gain_df = Rx_gain_df[(Rx_gain_df['RF_FREQ']>=21) & (Rx_gain_df['RF_FREQ']<=38)]

    stat_rx = Rx_gain_df.groupby("RF_FREQ").describe()
    stat_tx = Tx_Pout_df.groupby("RF_FREQ_OUT").describe(include='all')
    freq = list(stat_rx.index)

    lower_limits = -59
    upper_limits = -3
    tx_data_mean = list(stat_tx['p_out_fsl_dBm_']['mean'])
    #
    tx_data_std = list(stat_tx['p_out_fsl_dBm_']['std'])
    tx_data_max = list(stat_tx['p_out_fsl_dBm_']['max'])
    tx_data_min = list(stat_tx['p_out_fsl_dBm_']['min'])
    cond = [(Rx_gain_df["RF_FREQ"] == i) for i in freq]
    id_xer = 1 #len(id_list * number of ports) 19*8
    Rx_gain_df['Mean_Pout'] = np.select(cond,tx_data_mean*id_xer)
    Rx_gain_df['std_Pout'] = np.select(cond,tx_data_std*id_xer)

    Rx_gain_df['Max_Pout'] = np.select(cond,tx_data_max*id_xer)
    Rx_gain_df['Min_Pout'] = np.select(cond,tx_data_min*id_xer)
    Rx_gain_df['ADC_dBFS_mean_Max'] = Rx_gain_df['Mean_Pout']+Rx_gain_df['peak_gain_dB_']+ -51
    Rx_gain_df['ADC_dBFS_mean_Min'] = Rx_gain_df['Mean_Pout']+Rx_gain_df['peak_gain_dB_']+ -95
    selected_cols = ["RF_FREQ","RX_PORT","ADC_dBFS_mean_Max","ADC_dBFS_mean_Min"]#,"ADC_dBFS_max_Max","ADC_dBFS_max_Min","ADC_dBFS_min_Max","ADC_dBFS_min_Min"]
    df = Rx_gain_df[selected_cols]

    dfp = df.pivot_table(index='RF_FREQ', columns=['RX_PORT'],values = selected_cols)

    ax = dfp.plot.line(figsize=(11, 6))
    plt.axhline(y=upper_limits, color='g', linestyle='-')
    plt.axhline(y=lower_limits, color='r', linestyle='-')
    ax.get_legend().remove()
    plt.title("Dynamic Range")
    plt.ylabel("ADC_dBFS")
    plt.grid()
    name = "ReceiverDynamicRange"

    plt.savefig(f"img\{name}_{sn}.png")
