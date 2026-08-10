Test Parameters for WAM Bounce																			
RQ																			
	TEST NAME	WAM-C_BOUNCE																	
	SN	STD																	
																			
Index	Key	Vi Sequence	##KEY : 0 = DON’T RUN ;  1= RUN w/ FP open ; -1 = RUN w/ FP closed																
0	1	Setup vi Path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_BOUNCE_Setup.vi																
1	-1	Payload vi Path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_BOUNCE_Payload.vi																
2	1	Close vi Path	C:\RageATE-Tetra\Automated Tests\Tetra WAM\PRODUCTION\prod test vis\Tetra_BOUNCE_Close.vi																
																			
Index	Key	Input Constants	Units	Value		##KEY : KEY VALUES IGNORED for Constants													
0	0	COMPORT	Name		" Comport = ""COMx"" or Leave Blank for Auto-Detect"														
1	0	PS1-1 V;I	Volt : Amp	18.75;1	must use ;seperator # if 0 V selected here the PS will be ignored														
2	0	Cycle_Power	Bool	0															
3	0	Averages	num	1	If >1 will scan n times and use the mean														
4	0	SaveDataFiles	bool	1	"a ""1"" will create an iq file "														
5	0	Temp Soak	sec	0															
6	0	CMD	cmd;cmd		send commands prior to test. Leave Blank to skip														
7	0	Use Gantry	Bool	1															
8	0	Run_Clk_Test	Bool	1															
9	0	Clk_Test_Script	file	C:\RageATE-Tetra\Automated Tests\Tetra WAM\Utilities\VerifySiTime.py															
10	0	Clk_Test_Good	file	C:\RageATE-Tetra\Automated Tests\Tetra WAM\Utilities\ext_wamGood.txt															
																			
Index	Key	Loop Parameters	Units	Values	"##1… = LIST ; -2 = Ramp [Start,Stop,Step] ; -3 = File path (list of csv values starting at column 0 row 0) %% There is no option to skip so a value MUST be entered"														
0	1	TEMP	DEG	skip	-10	50	25												
1	1	PS1-1_V	VOLT	18.75															
2	1	TBD	tbd	1															
3	1	TBD	tbd	1															 
4	1	TBD	tbd	1															
5	1	TBD	tbd	1															
6	1	TBD	tbd	1															
7	1	TBD	tbd	1															
																			
Index	Key	Outputs	Value		##KEY : KEY VALUES IGNORED for Outputs														
1	1	ps1-1_dci	Amp																
2	1	power_w	Watt																
3	1	time	sec																
4	1	ess_fault	bool																
5	1	msn	dut sn																
6	1	pass/fail	bool																
7	1	ampl_0	db																
8	1	ampl_1	db																
9	1	ampl_2	db																
10	1	ampl_3	db																
11	1	ampl_4	db																
12	1	ampl_5	db																
13	1	ampl_6	db																
14	1	ampl_7	db																
15	1	ampl_8	db																
16	1	ampl_9	db																
17	1	ampl_10	db																
18	1	ampl_11	db																
19	1	ampl_12	db																
20	1	ampl_13	db																
21	1	ampl_14	db																
22	1	ampl_15	db																
23	1	ampl_16	db																
24	1	ampl_17	db																
25	1	ampl_18	db																
26	1	ampl_19	db																
27	1	ampl_20	db																
28	1	ampl_21	db																
29	1	ampl_22	db																
30	1	ampl_23	db																
31	1	ampl_24	db																
32	1	ampl_25	db																
33	1	ampl_26	db																
34	1	ampl_27	db																
35	1	ampl_28	db																
36	1	ampl_29	db																
37	1	ampl_30	db																
38	1	ampl_31	db																
39	1	ampl_32	db																
40	1	ampl_33	db																
41	1	ampl_34	db																
42	1	ampl_35	db																
43	1	ampl_36	db																
44	1	ampl_37	db																
45	1	ampl_38	db																
46	1	ampl_39	db																
47	1	ampl_40	db																
48	1	ampl_41	db																
49	1	freq_0	MHz																
50	1	freq_1	MHz																
51	1	freq_2	MHz																
52	1	freq_3	MHz																
53	1	freq_4	MHz																
54	1	freq_5	MHz																
55	1	freq_6	MHz																
56	1	freq_7	MHz																
57	1	freq_8	MHz																
58	1	freq_9	MHz																
59	1	freq_10	MHz																
60	1	freq_11	MHz																
61	1	freq_12	MHz																
62	1	freq_13	MHz																
63	1	freq_14	MHz																
64	1	freq_15	MHz																
65	1	freq_16	MHz																
66	1	freq_17	MHz																
67	1	freq_18	MHz																
68	1	freq_19	MHz																
69	1	freq_20	MHz																
70	1	freq_21	MHz																
71	1	freq_22	MHz																
72	1	freq_23	MHz																
73	1	freq_24	MHz																
74	1	freq_25	MHz																
75	1	freq_26	MHz																
76	1	freq_27	MHz																
77	1	freq_28	MHz																
78	1	freq_29	MHz																
79	1	freq_30	MHz																
80	1	freq_31	MHz																
81	1	freq_32	MHz																
82	1	freq_33	MHz																
83	1	freq_34	MHz																
84	1	freq_35	MHz																
85	1	freq_36	MHz																
86	1	freq_37	MHz																
87	1	freq_38	MHz																
88	1	freq_39	MHz																
89	1	freq_40	MHz																
90	1	freq_41	MHz																
91	1	iq_file	path																
92	1	ClkTest	PASS/FAIL																
																			
		End Parameters																	
