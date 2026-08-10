Test Parameters for Tetra TX																			
RQ																			
	TEST NAME	REV-C_P-WAM_TX-ATTEN																	
	SN	P0030																	
																			
Index	Key	Vi Sequence	##KEY : 0 = DON’T RUN ;  1= RUN w/ FP open ; -1 = RUN w/ FP closed																
0	1	Setup vi Path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_TX-ATTEN_Setup.vi																
1	-1	Payload vi Path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_TX-ATTEN_Payload.vi																
2	0	Close vi Path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_TX-PROD_Close.vi																
																			
Index	Key	Input Constants	Units	Value		##KEY : KEY VALUES IGNORED for Constants													
0	0	PS1-1 V;I	Volt : Amp	18.75;1	must use ;seperator # if 0 V selected here the PS will be ignored														
1	0	PS1-2 V:I	Volt : Amp	5;1	must use ;seperator # if 0 V selected here the PS will be ignored														
2	0	COM PORT	STR																
3	0	MODE	Bool	0	NOT USED [0 = MAN |1 = AUTO(Freq driven test)]														
4	0	TXPORT;Antenna Dist	ant/inch	1;21	For Setup only . 0 = skip gantry														
5	0	TX Filt Cutoff	GHz	25	"if ""-1"" used for Tx filter, then the filt 2 to 3 crossover F (GHz)"														
6	0	Meas Plate Temp; Meas Chip Temp	Bool;Bool	0;0															
7	0	Meas DC PS;Meas DCMON (Chip)	Bool;Bool	0;0															
8	0	Meas H2 	Bool;Freq(GHz)	0;0	0 = DO NOT MEASURE ; 1 = Measure Freq(GHz)														
9	0	Meas H*x	Freq(GHz);multiplier	0;0	"If Freq;mult = 0;0 , do not measure.; Freq multiplier"					% will measure the frequency * multiplier at the specified RF Frequency in GHz									
10	0	Meas S11;TXPORT	Bool;num	0;0	"if""1"" will measure s11;measure S11 only on this port number (leave blank for all)"														
11	0	Read Detector (1-4) 	Bool	0															
12	0	cmd;…	cmd;cmd			txbpf 1	txbias 0 11;txbias 5 10			"for setup program. 1 time register writes, seperated by "";"" "									
13	0	Temp Soak Time	min	2	time to wait after ??? Setup or initialize # Not ready yet														
14	0	PNA State File (local)	Path	D:\State Files\WAM_PRODUCTION.csa															
15	0	ENA State File	Path																
16	0	ENA RBW	Hz	3000															
17	0	ENA #of AVGs	num	4															
18	0	ENA Ref Lvl	dB	-30															
19	0	ENA Span	MHz	0.1															
20	0	RFIN_CAL	path																
21	0	HORN_CAL	path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\Test Benches\Common\Horn_Gain_121322.csv															
22	0	OUTPUT_CAL	path	Obsolete. Use File in ATE Specific folder															
23	0	FSL_APPLY	bool	1															
24	0	DCW_LIMITS	lsl;hsl	5;18															
25	0	POUT_LIMITS	lsl;hsl	0;10															
26	0	S11_LIMITS	lsl;hsl	-99;-10															
27	0	H2_LIMIT	dBc	-20															
																			
Index	Key	Loop Parameters	Units	Values	"##1… = LIST ; -2 = Ramp [Start,Stop,Step] ; -3 = File path (list of csv values starting at column 0 row 0) %% There is no option to skip so a value MUST be entered"														
0	1	TEMP	DEG	skip	-10	50	25												
1	1	PS1-1_V	VOLT	18.75															
2	1	RF_FREQ_OUT	GHZ	35	25	30	35	40											
3	3	TX_PORT	DBM	1	5	9													 
4	1	TX_FILT	num	-1															
5	1	ADAR_ATT	DB	8	8	15.5													
6	8	PSA_ATT	DB	0	0.5	1	2	4	8	16	31.5								
7	1	REF_POWER		12.5															
																			
Index	Key	Outputs	Value		##KEY : KEY VALUES IGNORED for Outputs														
1	1	ps1-1_dci	Amp																
2	1	power_w	Watt																
3	1	f_peak	MHz																
4	1	p_out_raw	dBm																
5	1	p_out_corr	dBm																
6	1	p_out_fsl	dBm																
7	1	s11	db																
8	1	ref_freq	GHz																
9	1	h2_peak	MHz																
10	1	h2_pout	dBm																
11	1	h2_pout_corr	dBm																
12	1	h2_dbc	dbc																
13	1	hx_peak	ghz																
14	1	hx_pout	dbm																
15	1	hx_pout_corr	dbm																
16	1	hx_dbc	dbc																
17	1	det_out	num																
18	1	filt_out	num																
19	1	bpf_out	num																
20	1	adar-att val	num																
21	1	ext-att-val	num																
22	1	a0_value	num																
23	1	a1_value	num																
24	1	a2_value	num																
25	1	a3_value	num																
26	1	prot_18p5	volt																
27	1	core_1p0	volt																
28	1	xvr_1p0	volt																
29	1	dig_1p8	volt																
30	1	dig_3p3	volt																
31	1	xvr_1p2	volt																
32	1	div_5p0	volt																
33	1	3p3v	volt																
34	1	rx_2p5	volt																
35	1	tx_2p5	volt																
36	1	adc_1p8	volt																
37	1	sw_3p6	volt																
38	1	sw_5p5	volt																
39	1	sw_2p8a	volt																
40	1	sw_2p8b	volt																
41	1	sw_2p4	volt																
42	1	sw_1p4	volt																
43	1	sw_3p6	amp																
44	1	sw_5p5	amp																
45	1	sw_2p8a	amp																
46	1	sw_2p8b	amp																
47	1	sw_2p4	amp																
48	1	sw_1p4	amp																
49	1	adar_temp	deg_c																
50	1	fpga_temp	deg_c																
51	1	ext_temp1	deg_c																
52	1	ext_temp2	deg_c																
53	1	ext_temp3	deg_c																
54	1	ext_temp4	deg_c																
55	1	temp_sense1	deg_c																
56	1	temp_sense2	deg_c																
57	1	time	sec																
58	1	Iteration	count																
59	1	rf_cal_ampl	dB																
60	1	rf_cal_freq	MHz																
61	1	h2_cal_ampl	dB																
62	1	h2_cal_freq	MHz																
63	1	hx_cal_ampl	ghz																
64	1	hx_cal_freq	db																
65	1	fsl_ampl_corr	dB																
66	1	fsl_loss_db	dB																
67	1	horn_gain_db	dB																
68	1	sn	ser #																
69	1	cmd	spi word																
70	1	adar_temp	Hex 																
71	1	dcw_hsl	Watt																
72	1	dcw_lsl	Watt																
73	1	dcw_pass	Bool																
74	1	dcv_pass	Bool																
75	1	p_out_hsl	dBm																
76	1	p_out_lsl	dBm																
77	1	p_out_pass	Bool																
78	1	att_dnl	dB																
79	1	psa_hsl	dB																
80	1	psa_lsl	dB																
81	1	atten_pass	Bool																
82	1	pass/fail	Bool																
83	1	ess_fault	Bool																
																			
		End Parameters																	
