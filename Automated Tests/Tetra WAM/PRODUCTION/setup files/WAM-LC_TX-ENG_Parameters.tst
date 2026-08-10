Test Parameters for Tetra TX																			
RQ																			
	TEST NAME	REV-LC_TETRA_TX-ENG																	
	SN	P0030																	
																			
Index	Key	Vi Sequence	##KEY : 0 = DON’T RUN ;  1= RUN w/ FP open ; -1 = RUN w/ FP closed																
0	1	Setup vi Path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_TX-PROD_Setup.vi																
1	-1	Payload vi Path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_TX-PROD_Payload.vi																
2	1	Close vi Path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_TX-PROD_Close.vi																
																			
Index	Key	Input Constants	Units	Value		##KEY : KEY VALUES IGNORED for Constants													
0	0	PS1-1 V;I	Volt : Amp	18.75;1	must use ;seperator # if 0 V selected here the PS will be ignored														
1	0	PS1-2 V:I	Volt : Amp	5;1	must use ;seperator # if 0 V selected here the PS will be ignored														
2	0	COM PORT	STR		"leave blank to auto detect or force with ""COMx"""														
3	0	MODE	Bool	1	NOT USED [0 = MAN |1 = AUTO(Freq driven test)]														
4	0	TXPORT;Antenna Dist	ant/inch	1;21	For Setup only . 0 = skip gantry														
5	0	TX Filt Cutoff	GHz	25	"if ""-1"" used for Tx filter, then the filt 2 to 3 crossover F (GHz)"														
6	0	Meas Plate Temp; Meas Chip Temp	Bool;Bool	0;1	"IF = 0, Then will measure temp on : 1) 1st Iteration And 2) Every time a port change occurs. IF = 1 will every iteration"														
7	0	Meas DC PS;Meas DCMON (Chip)	Bool;Bool	1;1	"IF = 0, Then will measure temp on : 1) 1st Iteration And 2) Every time a port change occurs.IF = 1 will every iteration"														
8	0	Meas H2 	Bool;Freq(GHz)	1;20	0 = DO NOT MEASURE ; 1 = Measure Freq(GHz)														
9	0	Meas H*x	Freq(GHz);multiplier	40;0.5	"If Freq;mult = 0;0 , do not measure.; Freq multiplier"					% will measure the frequency * multiplier at the specified RF Frequency in GHz									
10	0	Meas S11;TXPORT	Bool;num	1;1	"if""1"" will measure s11;measure S11 only on this port number (leave blank for all)"														
11	0	Read Detector (1-4) 	Bool	0															
12	0	cmd;…	cmd;cmd		Commands that run in Setup 			"for setup program. 1 time register writes, seperated by "";"" "								txbpf 1	txbias 0 11;txbias 5 10		
13	0	Temp Soak Time	min	10	time to wait after Temperature is reached . Only used for temp testing														
14	0	PNA State File (local)	Path	D:\State Files\WAM_PRODUCTION.csa															
15	0	ENA State File	Path		Obsolete. May come back at some point. LEAVE BLANK														
16	0	ENA RBW	Hz	3000	Sets the RBW of the spectrum Analyzer														
17	0	ENA #of AVGs;Harmonic#of Avgs	num;num	4;32	"Sets the Number of Averages on the Spectrum Analyzer. First Avg is for fundumental, 2nd is for Harmonics H2 and Hx"														
18	0	ENA Ref Lvl	dB	-10	Sets the Lvl of the spectrum Analyzer														
19	0	ENA Span	MHz	0.1	Sets the span of the Spectrum Analyzer														
20	0	RFIN_CAL	path	Not Used	Reserved calibration file. 														
21	0	HORN_CAL	path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\Test Benches\Common\Horn_Gain_121322.csv															
22	0	OUTPUT_CAL	path	Obsolete. Use File in ATE Specific folder															
23	0	FSL_APPLY	bool	1	"If = 1 , then FSPL will be added to the measurement"														
24	0	DCW_LIMITS	lsl;hsl	5;18	DCWatts limits. PS measure of V x I														
25	0	POUT_LIMITS	lsl;hsl	-40;10	Output power Limits														
26	0	S11_LIMITS	lsl;hsl	-99;-1	Return loss Limits														
27	0	H2_LIMIT	dBc	-10	2nd Harmonic Limit														
28	0	TX_FLAT	dB	20	Flatness Limit. Always positive.														
29	0	SER_READ	cmd;cmd		serial readback performed at end of payload iteration														
																			
Index	Key	Loop Parameters	Units	Values	"##1… = LIST ; -2 = Ramp [Start,Stop,Step] ; -3 = File path (list of csv values starting at column 0 row 0) %% There is no option to skip so a value MUST be entered"														
0	1	TEMP	DEG	skip	-10	50	25												
1	1	PS1-1_V	VOLT	18.75															
2	-2	TX_PORT	NUM	1	12	1													
3	1	REF_POWER	DBM	12.5															 
4	1	TX_FILT	num	-1	3														
5	1	ADAR_ATT	DB	-1															
6	1	PSA_ATT	DB	-1															
7	-2	RF_FREQ_OUT	GHZ	20	40	0.1													
																			
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
39	1	sw_2p8	volt																
40	1	18p5_protect	volt																
41	1	sw_2p1	volt																
42	1	sw_1p4	volt																
43	1	sw_3p6	amp																
44	1	sw_5p5	amp																
45	1	sw_2p8	amp																
46	1	18p5_protect	amp																
47	1	sw_2p1	amp																
48	1	sw_1p4	amp																
49	1	adar_temp	deg_c																
50	1	int_temp	deg_c																
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
68	3	sn	ser #																
69	1	cmd	spi word																
70	1	TempSense	Hex 																
71	1	dc_hsl	Watt																
72	1	dc_lsl	Watt																
73	1	p_out_hsl	dBm																
74	1	p_out_lsl	dBm																
75	1	s11_hsl	db																
76	1	s11_lsl	db																
77	1	h2_lim	dbc																
78	1	dc|pout|s11|h2|TxFlat (p/f)	5b 																
79	1	pass/fail	Bool																
80	1	ess_fault	Bool																
81	1	TxFlat	dB																
82	1	pdc|s11|txf|txp (prod)	4b 																
83	1	Serial Readbacks	str																
84	1	file	path																
																			
		End Parameters																	
