Test Parameters for Tetra RX																			
RQ																			
	TEST NAME	REV-C_P-WAM_RX-PROD	##This will be the Directory Name under C:\RageATE Results																
	SN	P0030	## Will be part of filename. May be overwritten in result file with ESN query.																
																			
Index	Key	Vi Sequence	##KEY : 0 = DON’T RUN ;  1= RUN w/ FP open ; -1 = RUN w/ FP closed																
0	1	Setup vi Path	C:\RageATE\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_RX-PROD_Setup.vi																
1	-1	Payload vi Path	C:\RageATE\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_RX-PROD_Payload.vi																
2	1	Close vi Path	C:\RageATE\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_RX-PROD_Close.vi																
																			
Index	Key	Input Constants	Units	Value		##KEY : KEY VALUES IGNORED for Constants													
0	0	PS1-1 V;I	Volt ; Amp	18.75;1	must use ;seperator # if 0 V selected here the PS will be ignored														
1	0	PS1-2 V:I	Volt ; Amp	5;1	must use ;seperator # if 0 V selected here the PS will be ignored														
2	0	COMPORT	STR		"Comport used for serial connection to WAM Leave Blank for auto or ""COMx"" for force"														
3	0	MODE	Bool	1	"[0 = MAN |1 = AUTO] 1 = Frequency Driven Test ; cmd : ""rffreq "" will set filter and gain"														
4	0	RXPORT;Gantry Z	ant;inch	1;21	###Controls 2 actions (1)Sets the Gantry Location for setup. If 0 is selected the gantry will be ignored in setup. (2) Will set the Gantry Z position (Z only set one time during setup). FSPL is calculated using this number														
5	0	"[fixed ,sweep] ; [IF_FREQ(mhz), REF FREQ(ghz)]"	MHz/GHZ	fixed; -10	##use neg (-) for LO<RF ; If sweep is selected then enter a freq in GHZ that will hold the REF freq so you can sweep the RF and look at IF response.														
6	0	Temp Soak	min	2	###Enter Time to soak in minutes.														
7	0	Meas DC PS;Meas DCMON (Chip)	Bool	0;0	### for Psand DCMON; IF 1 then will capture DC on each iteration(only first iteration if 0)														
8	0	MEAS_SNR;BW	Bool;MHz	1;10	"0 = DO NOT MEASURE , 1 = Measure ; BW (MHZ)"														
9	0	Meas Temp Sensors;Meas Temp Plate	Bool	1;0	"Meas Temp Sensors if ""1"" , will get all the on board Temp data ; Meas Temp Plate if ""1"" will measure the 2 temp sensors that are connected to the Temp Plate System"														
10	0	Capture Rx Data	Bool	1	iF = 1 then will save entire Trace File														
11	0	RxFilter Cutoff Freq	GHz	25	"if > = then use filter 3. Else use filter 2. !! Must write filter = ""-1"" for RX_FILT loop"														
12	0	Cmd;Cmd…	cmd		"You can send commands to the device one time during the setup. Send multiple commands using a "";"" seperator. Leave blank to skip."														
13	0	# of Avgs Sig;Noise;NFOfsFreq	count	1;10;0	# of Avgs for Sig capture; Noise Capture; IF Freq Offset for Noise [offsets the lo for noise only]														
14	0	PNA State File (local)	Path	D:\State Files\WAM_PRODUCTION.csa	"The setup file the PNA looks for on the host computer. It is mapped as ""Z"" drive"														
15	0	RF_Cal_Path	Path	Obsolete. Cal File Auto Loads from folder	Calibration file for ATE. This is the calibration that was performed on the ATE tester.														
16	0	Horn_Cal_Path	Path	C:\RageATE\Automated Tests\Tetra WAM\PRODUCTION\Test Benches\Common\Horn_Gain_121322.csv	Horn Cal Path is a sort of static offset based on typical Antenna Loss for the horn antenna														
17	0	RX SNR FREQ LIST	List	20;21;25;30;35;40	;seperated list of frequencies to measure noise. (leave blank for all)														
18	0	ADC_DATA[0-Ser|1-Eth];ADC_RESYNC[1 = T]	Bool;Bool	1;1	ADC_DATA !! If 1 will use deser ethernet connection IF = 0 will use serial port capture ; ADC_RESYNC = 1!!WILL run cmd>adcsync -v if freq OR ADC is unlocked														
19	0	Apply FSPL Corr	Bool	1	"IF = 1, will apply calibration from FSPL. This will load the cal table into the Sig Gen."														
20	0	Run Cal ADC on Temp Change	Bool	1	"IF = 1 , Will run Cal ADC during setup AND at a temperature change if temp is selected"														
21	0	dBFS Reference Level	dB	-2	"Used to compute gain.Converts dBFS to dBm. Based on FS(ADC) = 0.98V, and ADC load of 191 ohms"														
22	0	DCW_lsl;hsl	W	5;18	Power in Watts SPEC														
23	0	Gain_LSL;HSL	dB	30;50	Gain Spec 														
24	0	NF_MASK	path	C:\RageATE\Automated Tests\Tetra WAM\PRODUCTION\Test Benches\Common\WAM_NF_MASK.txt	NF Spec														
25	0	ZipCapture;DeleteDirectory	Bool;Bool	1;1	ZipCapture [1 = create zip file from captured files];DeleteDirectory[1 = delete original folder (to save space)														
																			
Index	Key	Loop Parameters	Units	Values	"##1… = LIST ; -2 = Ramp [Start,Stop,Step] ; -3 = File path (list of csv values starting at column 0 row 0) %% There is no option to skip so a value MUST be entered"														
0	1	TEMP	DEG	skip		50	25	75											
1	1	PS1-1_V	VOLT	18.75															
2	-2	RX_PORT	NUM	1	8	1													
3	1	REF_POWER	DBM	12.5															 
4	1	RF_POWER	DBM	-73															
5	1	RX_FILT	NUM	-1				"#rxfilt 0 (off) 1 (low) 2 (mid) 3 (high) ""-1"" (use cutoff freq)"											
6	1	RX_GAIN	CODE	-1				# (-1) = Use the FW default											
7	-2	RF_FREQ	GHZ	20	40	0.1													
																			
Index	Key	Outputs	Value		##KEY : KEY VALUES IGNORED for Outputs														
1	1	ps1-1_dci	Amp																
2	1	power_w	Watt																
3	1	rxfilt_out	num																
4	1	bpf_out	num																
5	1	rxgain1	code																
6	1	rxgain2	code																
7	1	rxgain3	code																
8	1	rxgain4	code																
9	1	ref_freq	GHz																
10	1	if_freq	MHz																
11	1	peak_p	dBm																
12	1	peak_gain	dB																
13	1	peak_f	MHz																
14	1	bp_rfon	dBm/Hz																
15	1	bp_rfoff	dBm/Hz																
16	1	Pout_s-n	dB																
17	1	bp_fout	MHz(bin out)																
18	1	noisefig	dB																
19	1	prot_18p5	Volt																
20	1	core_1p0	Volt																
21	1	xvr_1p0	Volt																
22	1	dig_1p8	Volt																
23	1	dig_3p3	Volt																
24	1	xvr_1p2	Volt																
25	1	div_5p0	Volt																
26	1	3p3v	Volt																
27	1	rx_2p5	Volt																
28	1	tx_2p5	Volt																
29	1	adc_1p8	Volt																
30	1	sw_3p6	Volt																
31	1	sw_5p5	Volt																
32	1	sw_2p8a	Volt																
33	1	sw_2p8b	Volt																
34	1	sw_2p4	Volt																
35	1	sw_1p4	Volt																
36	1	sw_3p6	Amp																
37	1	sw_5p5	Amp																
38	1	sw_2p8a	Amp																
39	1	sw_2p8b	Amp																
40	1	sw_2p4	Amp																
41	1	sw_1p4	Amp																
42	1	temp-sense1	°C																
43	1	temp-sense2	°C																
44	1	adar_temp	deg_c																
45	1	fpga_temp	deg_c																
46	1	ext_temp1	deg_c																
47	1	ext_temp2	deg_c																
48	1	ext_temp3	deg_c																
49	1	ext_temp4	deg_c																
50	1	cal_rf_freq	MHz																
51	1	cal_rf_ampl	dB																
52	1	time	sec																
53	1	Iteration	count																
54	1	locked	bool																
55	1	abs_time	stamp																
56	1	sn	ser #																
57	1	trace_file_sig	path																
58	1	trace_file_noise	path																
59	1	adcsync	str																
60	1	adccal	str																
61	1	adc_chan_id	str																
62	1	adc_lock	bool																
63	1	adc_sync_num	num																
64	1	dcw_hsl	dB																
65	1	dcw_lsl	dB																
66	1	gain_hsl	dB																
67	1	gain_lsl	dB																
68	1	nf_hsl	dB																
69	1	nf_lsl	dB																
70	1	dc|gain|nf (p/f)	3b  bool 																
71	1	PASS/FAIL	Bool																
72	1	pdc|g|nf (prod)	3b  bool 																
																			
		End Parameters																	
