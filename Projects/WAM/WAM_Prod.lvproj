<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="18008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="RageATE" Type="Folder">
			<Item Name="Automated Tests" Type="Folder">
				<Item Name="Tetra WAM" Type="Folder">
					<Item Name="Comms" Type="Folder">
						<Item Name="Detect_FTDI-USBSerial.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Detect_FTDI-USBSerial.vi"/>
						<Item Name="DetectAndKillTeraterm.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/DetectAndKillTeraterm.vi"/>
						<Item Name="ReadTempSense.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/ReadTempSense.vi"/>
						<Item Name="RX-ADAR-TEMP.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/RX-ADAR-TEMP.vi"/>
						<Item Name="SerialArray.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/SerialArray.vi"/>
						<Item Name="SerRW-Array.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/SerRW-Array.vi"/>
						<Item Name="Tetra Serial.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra Serial.vi"/>
						<Item Name="Tetra-FPGA_Boot-Success.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra-FPGA_Boot-Success.vi"/>
						<Item Name="Tetra_ADC-Frame.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_ADC-Frame.vi"/>
						<Item Name="Tetra_AntSel.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_AntSel.vi"/>
						<Item Name="Tetra_Atten.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_Atten.vi"/>
						<Item Name="Tetra_BPF.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_BPF.vi"/>
						<Item Name="Tetra_CalAdc.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_CalAdc.vi"/>
						<Item Name="Tetra_ESN-NoCheck.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_ESN-NoCheck.vi"/>
						<Item Name="Tetra_Filt.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_Filt.vi"/>
						<Item Name="Tetra_Read Imon.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_Read Imon.vi"/>
						<Item Name="Tetra_Read UCD.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_Read UCD.vi"/>
						<Item Name="Tetra_ReadESN.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_ReadESN.vi"/>
						<Item Name="Tetra_Rev.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_Rev.vi"/>
						<Item Name="Tetra_RxGain.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_RxGain.vi"/>
						<Item Name="Tetra_Set-Freq.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_Set-Freq.vi"/>
						<Item Name="Tetra_TxReg_48.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra_TxReg_48.vi"/>
						<Item Name="TetraComms.aliases" Type="Document" URL="../../../Automated Tests/Tetra WAM/Comms/TetraComms.aliases"/>
						<Item Name="TetraComms.lvlps" Type="Document" URL="../../../Automated Tests/Tetra WAM/Comms/TetraComms.lvlps"/>
						<Item Name="TetraComms.lvproj" Type="Document" URL="../../../Automated Tests/Tetra WAM/Comms/TetraComms.lvproj"/>
						<Item Name="TX-ADAR-DETECT.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/TX-ADAR-DETECT.vi"/>
						<Item Name="TX-ADAR-TEMP.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/TX-ADAR-TEMP.vi"/>
						<Item Name="UCD_Device-Info.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/UCD_Device-Info.vi"/>
						<Item Name="SelfTest.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/SelfTest.vi"/>
						<Item Name="Tetra Serial FA.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tetra Serial FA.vi"/>
						<Item Name="Tx-RxFilt.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/Tx-RxFilt.vi"/>
						<Item Name="TX-ADAR-DETECT(LC).vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Comms/TX-ADAR-DETECT(LC).vi"/>
					</Item>
					<Item Name="PRODUCTION" Type="Folder">
						<Item Name="post processor" Type="Folder">
							<Item Name="FilterAndSortData.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/post processor/FilterAndSortData.vi"/>
							<Item Name="FinalReportResult.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/post processor/FinalReportResult.vi"/>
							<Item Name="FinalReportResult_GUI.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/post processor/FinalReportResult_GUI.vi"/>
							<Item Name="PostFinalTest.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/post processor/PostFinalTest.vi"/>
							<Item Name="Prod_Screen.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/post processor/Prod_Screen.vi"/>
							<Item Name="ProdLimits.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/post processor/ProdLimits.vi"/>
							<Item Name="Statistics.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/post processor/Statistics.vi"/>
							<Item Name="WAM_Database_log.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/post processor/WAM_Database_log.vi"/>
							<Item Name="WAM_Datalog Parser.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/post processor/WAM_Datalog Parser.vi"/>
						</Item>
						<Item Name="prod test vis" Type="Folder">
							<Item Name="ClkRegTest.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/ClkRegTest.vi"/>
							<Item Name="Tetra_BOUNCE_Close.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_BOUNCE_Close.vi"/>
							<Item Name="Tetra_BOUNCE_Payload.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_BOUNCE_Payload.vi"/>
							<Item Name="Tetra_BOUNCE_Setup.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_BOUNCE_Setup.txt"/>
							<Item Name="Tetra_BOUNCE_Setup.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_BOUNCE_Setup.vi"/>
							<Item Name="Tetra_PROD_Instruments.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_PROD_Instruments.vi"/>
							<Item Name="Tetra_RX-PROD_Close.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_RX-PROD_Close.vi"/>
							<Item Name="Tetra_RX-PROD_Payload.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_RX-PROD_Payload.vi"/>
							<Item Name="Tetra_RX-PROD_Setup.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_RX-PROD_Setup.txt"/>
							<Item Name="Tetra_RX-PROD_Setup.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_RX-PROD_Setup.vi"/>
							<Item Name="Tetra_TX-ATTEN_Payload.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_TX-ATTEN_Payload.vi"/>
							<Item Name="Tetra_TX-ATTEN_Setup.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_TX-ATTEN_Setup.vi"/>
							<Item Name="Tetra_TX-PROD_Close.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_TX-PROD_Close.vi"/>
							<Item Name="Tetra_TX-PROD_Payload.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_TX-PROD_Payload.vi"/>
							<Item Name="Tetra_TX-PROD_Setup.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/Tetra_TX-PROD_Setup.vi"/>
							<Item Name="txatten.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/txatten.txt"/>
							<Item Name="txflat.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/prod test vis/txflat.txt"/>
						</Item>
						<Item Name="setup files" Type="Folder">
							<Item Name="Rage_Equipment_Calibration.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/setup files/Rage_Equipment_Calibration.csv"/>
							<Item Name="WAM-C_BOUNCE.tst" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/setup files/WAM-C_BOUNCE.tst"/>
							<Item Name="WAM-C_RX-PROD-250M_Parameters.tst" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/setup files/WAM-C_RX-PROD-250M_Parameters.tst"/>
							<Item Name="WAM-C_TX-ATTEN_Parameters.tst" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/setup files/WAM-C_TX-ATTEN_Parameters.tst"/>
							<Item Name="WAM-C_TX-PROD-250M_Parameters.tst" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/setup files/WAM-C_TX-PROD-250M_Parameters.tst"/>
							<Item Name="WAM_RX-Startup.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/setup files/WAM_RX-Startup.txt"/>
							<Item Name="WAM_NF_MASK.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/setup files/WAM_NF_MASK.txt"/>
						</Item>
						<Item Name="Test Benches" Type="Folder">
							<Item Name="CalFiles" Type="Folder"/>
							<Item Name="Common" Type="Folder">
								<Item Name="CalPopupTimer.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/Common/CalPopupTimer.txt"/>
								<Item Name="Git_CheckList.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/Common/Git_CheckList.txt"/>
								<Item Name="Horn_Gain_121322-ArchiveCopy.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/Common/Horn_Gain_121322-ArchiveCopy.csv"/>
								<Item Name="Horn_Gain_121322.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/Common/Horn_Gain_121322.csv"/>
								<Item Name="Test_Bench.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/Common/Test_Bench.txt"/>
								<Item Name="TetraHornLoss.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/Common/TetraHornLoss.csv"/>
								<Item Name="WAM_PROD_TEST_Instruments.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/Common/WAM_PROD_TEST_Instruments.csv"/>
							</Item>
							<Item Name="WAM_PROD_TEST-1" Type="Folder">
								<Item Name="WAM_PROD_TEST-1 Calibration Files" Type="Folder">
									<Item Name="FSPL.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/WAM_PROD_TEST-1/WAM_PROD_TEST-1 Calibration Files/FSPL.csv"/>
									<Item Name="WAM_PROD_TEST-1_INPUT_042425-1145.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/WAM_PROD_TEST-1/WAM_PROD_TEST-1 Calibration Files/WAM_PROD_TEST-1_INPUT_042425-1145.csv"/>
									<Item Name="WAM_PROD_TEST-1_OUTPUT_042425-1145.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/WAM_PROD_TEST-1/WAM_PROD_TEST-1 Calibration Files/WAM_PROD_TEST-1_OUTPUT_042425-1145.csv"/>
									<Item Name="WAM_PROD_TEST-1_SG-FLAT_042425-1145.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/WAM_PROD_TEST-1/WAM_PROD_TEST-1 Calibration Files/WAM_PROD_TEST-1_SG-FLAT_042425-1145.csv"/>
								</Item>
							</Item>
							<Item Name="WAM_PROD_TEST-2" Type="Folder">
								<Item Name="WAM_PROD_TEST-2 Calibration Files" Type="Folder">
									<Item Name="WAM_PROD_TEST-2_INPUT_021425-1353.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/WAM_PROD_TEST-2/WAM_PROD_TEST-2 Calibration Files/WAM_PROD_TEST-2_INPUT_021425-1353.csv"/>
									<Item Name="WAM_PROD_TEST-2_OUTPUT_021425-1353.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/WAM_PROD_TEST-2/WAM_PROD_TEST-2 Calibration Files/WAM_PROD_TEST-2_OUTPUT_021425-1353.csv"/>
									<Item Name="WAM_PROD_TEST-2_SG-FLAT_021425-1353.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/WAM_PROD_TEST-2/WAM_PROD_TEST-2 Calibration Files/WAM_PROD_TEST-2_SG-FLAT_021425-1353.csv"/>
								</Item>
							</Item>
							<Item Name="CalFiles.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/CalFiles.txt"/>
							<Item Name="TestBenches.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/Test Benches/TestBenches.txt"/>
						</Item>
						<Item Name="WAM_Production.ini" Type="Document" URL="../../../Automated Tests/Tetra WAM/PRODUCTION/WAM_Production.ini"/>
					</Item>
					<Item Name="Utilities" Type="Folder">
						<Item Name="Cal Utilities" Type="Folder">
							<Item Name="ATE-CalPopup.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/ATE-CalPopup.vi"/>
							<Item Name="CalPoPup.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/CalPoPup.vi"/>
							<Item Name="CalWAM-Prod(BETA).vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/CalWAM-Prod(BETA).vi"/>
							<Item Name="Discover_Gantry_TestBench.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/Discover_Gantry_TestBench.vi"/>
							<Item Name="Discover_MXA.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/Discover_MXA.vi"/>
							<Item Name="Discover_MXG.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/Discover_MXG.vi"/>
							<Item Name="Discover_PNA.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/Discover_PNA.vi"/>
							<Item Name="Discover_Switch.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/Discover_Switch.vi"/>
							<Item Name="FindMostRecentCalFile.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/FindMostRecentCalFile.vi"/>
							<Item Name="PathSelectPopUp.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/PathSelectPopUp.vi"/>
							<Item Name="PNA_CalFile_Check.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/PNA_CalFile_Check.vi"/>
							<Item Name="FactoryCalPopupTimeDelay.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Cal Utilities/FactoryCalPopupTimeDelay.vi"/>
						</Item>
						<Item Name="Power Spectrum" Type="Folder">
							<Item Name="__pycache__" Type="Folder">
								<Item Name="plot.cpython-36.pyc" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/Power Spectrum/__pycache__/plot.cpython-36.pyc"/>
							</Item>
							<Item Name="plot.py" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/Power Spectrum/plot.py"/>
							<Item Name="PlotSpectrum.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Power Spectrum/PlotSpectrum.vi"/>
							<Item Name="Requirements" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/Power Spectrum/Requirements"/>
							<Item Name="sample_data.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/Power Spectrum/sample_data.csv"/>
							<Item Name="trace.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/Power Spectrum/trace.csv"/>
						</Item>
						<Item Name="Am_Init.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Am_Init.vi"/>
						<Item Name="BarCode.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/BarCode.txt"/>
						<Item Name="DcPreBootTest.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/DcPreBootTest.vi"/>
						<Item Name="DUTBarCode_Parser.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/DUTBarCode_Parser.vi"/>
						<Item Name="DynamicScanLinitParser.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/DynamicScanLinitParser.vi"/>
						<Item Name="Ecal-Manual-2.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Ecal-Manual-2.vi"/>
						<Item Name="Employee_Lookup(py).vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Employee_Lookup(py).vi"/>
						<Item Name="EnterDUTInfo.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/EnterDUTInfo.vi"/>
						<Item Name="ESN_Master_Table.csv" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/ESN_Master_Table.csv"/>
						<Item Name="ESNLookup.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/ESNLookup.vi"/>
						<Item Name="ext_wamGood.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/ext_wamGood.txt"/>
						<Item Name="ExtStd_wamGood.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/ExtStd_wamGood.txt"/>
						<Item Name="Gantry_GUI.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Gantry_GUI.vi"/>
						<Item Name="Gantry_GUI_Events.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Gantry_GUI_Events.vi"/>
						<Item Name="GetRxData.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/GetRxData.vi"/>
						<Item Name="CloseComAndFt.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/CloseComAndFt.vi"/>
						<Item Name="GetRxPower-Debug.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/GetRxPower-Debug.vi"/>
						<Item Name="GetRxPower.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/GetRxPower.vi"/>
						<Item Name="InputClk_Status.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/InputClk_Status.vi"/>
						<Item Name="int_wamGood.txt" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/int_wamGood.txt"/>
						<Item Name="LabViewScanResultParser.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/LabViewScanResultParser.vi"/>
						<Item Name="LeidosBarCode_DataBaseParser.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/LeidosBarCode_DataBaseParser.vi"/>
						<Item Name="N6700_PowerSupplyGUI.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/N6700_PowerSupplyGUI.vi"/>
						<Item Name="PingTestBoard.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/PingTestBoard.vi"/>
						<Item Name="Pll_Lock_Detect.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Pll_Lock_Detect.vi"/>
						<Item Name="PlotRxPower.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/PlotRxPower.vi"/>
						<Item Name="Port To Atten Map.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Port To Atten Map.vi"/>
						<Item Name="Pre-FinalTestBcScan.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Pre-FinalTestBcScan.vi"/>
						<Item Name="PSA-Mask.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/PSA-Mask.vi"/>
						<Item Name="PSA-MaskArray.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/PSA-MaskArray.vi"/>
						<Item Name="ReadAndParsePyFile.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/ReadAndParsePyFile.vi"/>
						<Item Name="Report Tool2.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Report Tool2.vi"/>
						<Item Name="WAM-DC-HealthCheck.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/WAM-DC-HealthCheck.vi"/>
						<Item Name="RfSwitch_GUI.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/RfSwitch_GUI.vi"/>
						<Item Name="Tetra_ImonFullTest.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Tetra_ImonFullTest.vi"/>
						<Item Name="Tetra_VmonFullTest.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/Tetra_VmonFullTest.vi"/>
						<Item Name="USER_BarCode_Popup.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/USER_BarCode_Popup.vi"/>
						<Item Name="WAM_BarCode_PopupWithPhoto.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/WAM_BarCode_PopupWithPhoto.vi"/>
						<Item Name="WAM_BarCode_Prompt.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/WAM_BarCode_Prompt.vi"/>
						<Item Name="WAM_RADIO_BUTTONS.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/WAM_RADIO_BUTTONS.vi"/>
						<Item Name="WAM_SN_Prompt.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/WAM_SN_Prompt.vi"/>
						<Item Name="WAM_UserBarCode_Popup.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/WAM_UserBarCode_Popup.vi"/>
						<Item Name="WAM_UserInfo_Prompt.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/WAM_UserInfo_Prompt.vi"/>
						<Item Name="WAM_UserInput_Popup.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/WAM_UserInput_Popup.vi"/>
						<Item Name="VerifySiTime.py" Type="Document" URL="../../../Automated Tests/Tetra WAM/Utilities/VerifySiTime.py"/>
						<Item Name="WriteCalInfoToInst.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/WriteCalInfoToInst.vi"/>
					</Item>
					<Item Name="Tetra_Globals.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Tetra_Globals.vi"/>
				</Item>
			</Item>
			<Item Name="Calibration" Type="Folder">
				<Item Name="GetCalData.vi" Type="VI" URL="../../../Calibration/GetCalData.vi"/>
				<Item Name="Search 1D Array for Nearest LV2012 NIVerified.vi" Type="VI" URL="../../../Calibration/Search 1D Array for Nearest LV2012 NIVerified.vi"/>
				<Item Name="SetupSpectrumAnalyzerForCal.vi" Type="VI" URL="../../../Calibration/SetupSpectrumAnalyzerForCal.vi"/>
				<Item Name="SpecAnMeasCW_Cal.vi" Type="VI" URL="../../../Calibration/SpecAnMeasCW_Cal.vi"/>
				<Item Name="TestStandCal.aliases" Type="Document" URL="../../../Calibration/TestStandCal.aliases"/>
				<Item Name="TestStandCal.lvlps" Type="Document" URL="../../../Calibration/TestStandCal.lvlps"/>
				<Item Name="TestStandCal.lvproj" Type="Document" URL="../../../Calibration/TestStandCal.lvproj"/>
			</Item>
			<Item Name="DLLs" Type="Folder">
				<Item Name="FTDI_UART" Type="Folder">
					<Item Name="prefix.inf" Type="Document" URL="../../../DLLs/FTDI_UART/prefix.inf"/>
				</Item>
				<Item Name="FTuArt.inf" Type="Document" URL="../../../DLLs/FTuArt.inf"/>
				<Item Name="mcl_pm64.dll" Type="Document" URL="../../../DLLs/mcl_pm64.dll"/>
			</Item>
			<Item Name="Infrastructure" Type="Folder">
				<Item Name="ArchiveResults.vi" Type="VI" URL="../../../Infrastructure/ArchiveResults.vi"/>
				<Item Name="BuildResultFilename.vi" Type="VI" URL="../../../Infrastructure/BuildResultFilename.vi"/>
				<Item Name="BuildResultsDirectoryPath.vi" Type="VI" URL="../../../Infrastructure/BuildResultsDirectoryPath.vi"/>
				<Item Name="BuildStrings_Return.vi" Type="VI" URL="../../../Infrastructure/BuildStrings_Return.vi"/>
				<Item Name="Computerlist.csv" Type="Document" URL="../../../Infrastructure/Computerlist.csv"/>
				<Item Name="computername.vi" Type="VI" URL="../../../Infrastructure/computername.vi"/>
				<Item Name="For Range.vi" Type="VI" URL="../../../Infrastructure/For Range.vi"/>
				<Item Name="Generate Test Parameter Globals_1.0.0.vi" Type="VI" URL="../../../Infrastructure/Generate Test Parameter Globals_1.0.0.vi"/>
				<Item Name="GenerateHeaderAndFilename.vi" Type="VI" URL="../../../Infrastructure/GenerateHeaderAndFilename.vi"/>
				<Item Name="Get Date and Time (sec).vi" Type="VI" URL="../../../Infrastructure/Get Date and Time (sec).vi"/>
				<Item Name="Get Time Only No Spaces.vi" Type="VI" URL="../../../Infrastructure/Get Time Only No Spaces.vi"/>
				<Item Name="Get_computername.vi" Type="VI" URL="../../../Infrastructure/Get_computername.vi"/>
				<Item Name="GetLoopParameters.vi" Type="VI" URL="../../../Infrastructure/GetLoopParameters.vi"/>
				<Item Name="Looper.vi" Type="VI" URL="../../../Infrastructure/Looper.vi"/>
				<Item Name="Looper_str.vi" Type="VI" URL="../../../Infrastructure/Looper_str.vi"/>
				<Item Name="make_current_default.vi" Type="VI" URL="../../../Infrastructure/make_current_default.vi"/>
				<Item Name="NumberToString_1.0.0.vi" Type="VI" URL="../../../Infrastructure/NumberToString_1.0.0.vi"/>
				<Item Name="NumToBinWord.vi" Type="VI" URL="../../../Infrastructure/NumToBinWord.vi"/>
				<Item Name="Open_Results_File_Excel.vi" Type="VI" URL="../../../Infrastructure/Open_Results_File_Excel.vi"/>
				<Item Name="RageAte_Delay_w-ProgressBar-2.vi" Type="VI" URL="../../../Infrastructure/RageAte_Delay_w-ProgressBar-2.vi"/>
				<Item Name="RageAte_Delay_w-ProgressBar.vi" Type="VI" URL="../../../Infrastructure/RageAte_Delay_w-ProgressBar.vi"/>
				<Item Name="RageATE_Send Email using SMTP Client.vi" Type="VI" URL="../../../Infrastructure/RageATE_Send Email using SMTP Client.vi"/>
				<Item Name="RageErrorCodes.csv" Type="Document" URL="../../../Infrastructure/RageErrorCodes.csv"/>
				<Item Name="RageErrorCodes.vi" Type="VI" URL="../../../Infrastructure/RageErrorCodes.vi"/>
				<Item Name="RageFileDialog.vi" Type="VI" URL="../../../Infrastructure/RageFileDialog.vi"/>
				<Item Name="Read_Value_From_Excel.vi" Type="VI" URL="../../../Infrastructure/Read_Value_From_Excel.vi"/>
				<Item Name="Save Current Value as Default.vi" Type="VI" URL="../../../Infrastructure/Save Current Value as Default.vi"/>
				<Item Name="SaveControlValues.vi" Type="VI" URL="../../../Infrastructure/SaveControlValues.vi"/>
				<Item Name="SendSMTP_Email.vi" Type="VI" URL="../../../Infrastructure/SendSMTP_Email.vi"/>
				<Item Name="SendSMTP_Email_2.vi" Type="VI" URL="../../../Infrastructure/SendSMTP_Email_2.vi"/>
				<Item Name="String-NumberToBool.vi" Type="VI" URL="../../../Infrastructure/String-NumberToBool.vi"/>
				<Item Name="StringToBool_Ctl._7b.vi" Type="VI" URL="../../../Infrastructure/StringToBool_Ctl._7b.vi"/>
				<Item Name="StringToBool_Ctl.vi" Type="VI" URL="../../../Infrastructure/StringToBool_Ctl.vi"/>
				<Item Name="StringToBool_Ctl_2.vi" Type="VI" URL="../../../Infrastructure/StringToBool_Ctl_2.vi"/>
				<Item Name="StringToBool_Ctl_3.vi" Type="VI" URL="../../../Infrastructure/StringToBool_Ctl_3.vi"/>
				<Item Name="StringToBool_Ctl_6b.vi" Type="VI" URL="../../../Infrastructure/StringToBool_Ctl_6b.vi"/>
				<Item Name="StringToNumberControl.vi" Type="VI" URL="../../../Infrastructure/StringToNumberControl.vi"/>
				<Item Name="StringToNumberControlWithBool(x2).vi" Type="VI" URL="../../../Infrastructure/StringToNumberControlWithBool(x2).vi"/>
				<Item Name="StringToNumberControlWithBool.vi" Type="VI" URL="../../../Infrastructure/StringToNumberControlWithBool.vi"/>
				<Item Name="SystemTestIterator.vi" Type="VI" URL="../../../Infrastructure/SystemTestIterator.vi"/>
				<Item Name="TempControlWithBool.vi" Type="VI" URL="../../../Infrastructure/TempControlWithBool.vi"/>
				<Item Name="Temperature Globals.vi" Type="VI" URL="../../../Infrastructure/Temperature Globals.vi"/>
				<Item Name="Test Parameter Globals_1.0.0.vi" Type="VI" URL="../../../Infrastructure/Test Parameter Globals_1.0.0.vi"/>
				<Item Name="Test Parameters.tmp" Type="Document" URL="../../../Infrastructure/Test Parameters.tmp"/>
				<Item Name="Test Result File Name Global.vi" Type="VI" URL="../../../Infrastructure/Test Result File Name Global.vi"/>
				<Item Name="TimeOutPopUp.vi" Type="VI" URL="../../../Infrastructure/TimeOutPopUp.vi"/>
				<Item Name="TimeToString.vi" Type="VI" URL="../../../Infrastructure/TimeToString.vi"/>
				<Item Name="Write Test Log.vi" Type="VI" URL="../../../Infrastructure/Write Test Log.vi"/>
				<Item Name="CleanUpArray.vi" Type="VI" URL="../../../Infrastructure/CleanUpArray.vi"/>
			</Item>
			<Item Name="Initialize References" Type="Folder">
				<Item Name="DestroyStationReferences.vi" Type="VI" URL="../../../Initialize References/DestroyStationReferences.vi"/>
				<Item Name="Discover DMM Model.vi" Type="VI" URL="../../../Initialize References/Discover DMM Model.vi"/>
				<Item Name="Discover Gantry.vi" Type="VI" URL="../../../Initialize References/Discover Gantry.vi"/>
				<Item Name="Discover Inst Model.vi" Type="VI" URL="../../../Initialize References/Discover Inst Model.vi"/>
				<Item Name="Discover Network Analyzer Model.vi" Type="VI" URL="../../../Initialize References/Discover Network Analyzer Model.vi"/>
				<Item Name="Discover NFA Model.vi" Type="VI" URL="../../../Initialize References/Discover NFA Model.vi"/>
				<Item Name="Discover Oven Model.vi" Type="VI" URL="../../../Initialize References/Discover Oven Model.vi"/>
				<Item Name="Discover PNA Model.vi" Type="VI" URL="../../../Initialize References/Discover PNA Model.vi"/>
				<Item Name="Discover Power Supply GPIB.vi" Type="VI" URL="../../../Initialize References/Discover Power Supply GPIB.vi"/>
				<Item Name="Discover Power Supply Model.vi" Type="VI" URL="../../../Initialize References/Discover Power Supply Model.vi"/>
				<Item Name="Discover RF Switch Model.vi" Type="VI" URL="../../../Initialize References/Discover RF Switch Model.vi"/>
				<Item Name="Discover Signal Generator Model.vi" Type="VI" URL="../../../Initialize References/Discover Signal Generator Model.vi"/>
				<Item Name="Discover Spectrum Analyzer Model.vi" Type="VI" URL="../../../Initialize References/Discover Spectrum Analyzer Model.vi"/>
				<Item Name="Discover USB Signal Generator Model.vi" Type="VI" URL="../../../Initialize References/Discover USB Signal Generator Model.vi"/>
				<Item Name="Discover USB-RF Switch.vi" Type="VI" URL="../../../Initialize References/Discover USB-RF Switch.vi"/>
				<Item Name="INST GLOBAL.vi" Type="VI" URL="../../../Initialize References/INST GLOBAL.vi"/>
				<Item Name="Instruments - TCPIP.csv" Type="Document" URL="../../../Initialize References/Instruments - TCPIP.csv"/>
				<Item Name="Instruments.csv" Type="Document" URL="../../../Initialize References/Instruments.csv"/>
				<Item Name="Open vi Reference_2.1.0.0.vi" Type="VI" URL="../../../Initialize References/Open vi Reference_2.1.0.0.vi"/>
				<Item Name="Open vi Reference_2.2.0.0.vi" Type="VI" URL="../../../Initialize References/Open vi Reference_2.2.0.0.vi"/>
				<Item Name="Open vi Reference_3.0.0.0.vi" Type="VI" URL="../../../Initialize References/Open vi Reference_3.0.0.0.vi"/>
				<Item Name="Sequence Globals.vi" Type="VI" URL="../../../Initialize References/Sequence Globals.vi"/>
				<Item Name="Station References Global.vi" Type="VI" URL="../../../Initialize References/Station References Global.vi"/>
				<Item Name="CallVi.vi" Type="VI" URL="../../../Initialize References/CallVi.vi"/>
			</Item>
			<Item Name="Labview Utilities" Type="Folder">
				<Item Name="GitTools" Type="Folder">
					<Item Name="GitFetch.vi" Type="VI" URL="../../../Labview Utilities/GitTools/GitFetch.vi"/>
					<Item Name="GitLog.vi" Type="VI" URL="../../../Labview Utilities/GitTools/GitLog.vi"/>
					<Item Name="GitPull.vi" Type="VI" URL="../../../Labview Utilities/GitTools/GitPull.vi"/>
					<Item Name="GitStatus.vi" Type="VI" URL="../../../Labview Utilities/GitTools/GitStatus.vi"/>
					<Item Name="GitPathList.vi" Type="VI" URL="../../../Labview Utilities/GitTools/GitPathList.vi"/>
				</Item>
				<Item Name="Hyper Terminal" Type="Folder">
					<Item Name="EXE" Type="Folder">
						<Item Name="Hyper Terminal.aliases" Type="Document" URL="../../../Labview Utilities/Hyper Terminal/EXE/Hyper Terminal.aliases"/>
						<Item Name="Hyper Terminal.exe" Type="Document" URL="../../../Labview Utilities/Hyper Terminal/EXE/Hyper Terminal.exe"/>
						<Item Name="Hyper Terminal.ini" Type="Document" URL="../../../Labview Utilities/Hyper Terminal/EXE/Hyper Terminal.ini"/>
						<Item Name="niwebserver.conf" Type="Document" URL="../../../Labview Utilities/Hyper Terminal/EXE/niwebserver.conf"/>
					</Item>
					<Item Name="Sub VI" Type="Folder">
						<Item Name="State Machine LLB.llb" Type="Folder">
							<Item Name="AddTriggeredEventsToStates.vi" Type="VI" URL="../../../Labview Utilities/Hyper Terminal/Sub VI/State Machine LLB.llb/AddTriggeredEventsToStates.vi"/>
							<Item Name="Current VIs Parents Ref__ogtk.vi" Type="VI" URL="../../../Labview Utilities/Hyper Terminal/Sub VI/State Machine LLB.llb/Current VIs Parents Ref__ogtk.vi"/>
							<Item Name="Error Handler.vi" Type="VI" URL="../../../Labview Utilities/Hyper Terminal/Sub VI/State Machine LLB.llb/Error Handler.vi"/>
							<Item Name="Fit VI window to Largest Dec__ogtk.vi" Type="VI" URL="../../../Labview Utilities/Hyper Terminal/Sub VI/State Machine LLB.llb/Fit VI window to Largest Dec__ogtk.vi"/>
							<Item Name="GetCurrentState.vi" Type="VI" URL="../../../Labview Utilities/Hyper Terminal/Sub VI/State Machine LLB.llb/GetCurrentState.vi"/>
							<Item Name="State Machine.vi" Type="VI" URL="../../../Labview Utilities/Hyper Terminal/Sub VI/State Machine LLB.llb/State Machine.vi"/>
						</Item>
						<Item Name="Prabhakant_Find_Serial_Port.vi" Type="VI" URL="../../../Labview Utilities/Hyper Terminal/Sub VI/Prabhakant_Find_Serial_Port.vi"/>
					</Item>
					<Item Name="Hyper Terminal.aliases" Type="Document" URL="../../../Labview Utilities/Hyper Terminal/Hyper Terminal.aliases"/>
					<Item Name="Hyper Terminal.lvlps" Type="Document" URL="../../../Labview Utilities/Hyper Terminal/Hyper Terminal.lvlps"/>
					<Item Name="Hyper Terminal.lvproj" Type="Document" URL="../../../Labview Utilities/Hyper Terminal/Hyper Terminal.lvproj"/>
					<Item Name="Hyper Terminal.vi" Type="VI" URL="../../../Labview Utilities/Hyper Terminal/Hyper Terminal.vi"/>
					<Item Name="HyperTerminal.doc" Type="Document" URL="../../../Labview Utilities/Hyper Terminal/HyperTerminal.doc"/>
					<Item Name="HyperTerminal.pdf" Type="Document" URL="../../../Labview Utilities/Hyper Terminal/HyperTerminal.pdf"/>
					<Item Name="readme.txt" Type="Document" URL="../../../Labview Utilities/Hyper Terminal/readme.txt"/>
				</Item>
				<Item Name="Parallel Port Switch.llb" Type="Folder">
					<Item Name="in-outport.vi" Type="VI" URL="../../../Labview Utilities/Parallel Port Switch.llb/in-outport.vi"/>
					<Item Name="Input Word From Port.vi" Type="VI" URL="../../../Labview Utilities/Parallel Port Switch.llb/Input Word From Port.vi"/>
					<Item Name="main.vi" Type="VI" URL="../../../Labview Utilities/Parallel Port Switch.llb/main.vi"/>
					<Item Name="Output Word To Port.vi" Type="VI" URL="../../../Labview Utilities/Parallel Port Switch.llb/Output Word To Port.vi"/>
				</Item>
				<Item Name="TCP-Tools" Type="Folder">
					<Item Name="Raw_Socket_Ping" Type="Folder">
						<Item Name="_EnumProcesses.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/_EnumProcesses.vi"/>
						<Item Name="_GetSockOpt.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/_GetSockOpt.vi"/>
						<Item Name="_Select Single.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/_Select Single.vi"/>
						<Item Name="_SetSockOpt.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/_SetSockOpt.vi"/>
						<Item Name="_WSACleanup.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/_WSACleanup.vi"/>
						<Item Name="_WSASocket.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/_WSASocket.vi"/>
						<Item Name="_WSAStartup.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/_WSAStartup.vi"/>
						<Item Name="Decode &amp;wsadata.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Decode &amp;wsadata.vi"/>
						<Item Name="Decode Hops From TTL.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Decode Hops From TTL.vi"/>
						<Item Name="Decode ICMP Packet.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Decode ICMP Packet.vi"/>
						<Item Name="Decode IP Packet.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Decode IP Packet.vi"/>
						<Item Name="Decode Packet.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Decode Packet.vi"/>
						<Item Name="Decode Reply.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Decode Reply.vi"/>
						<Item Name="Get Reply.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Get Reply.vi"/>
						<Item Name="ICMP Packet Info.ctl" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/ICMP Packet Info.ctl"/>
						<Item Name="Init Ping Packet.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Init Ping Packet.vi"/>
						<Item Name="Interpret Error.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Interpret Error.vi"/>
						<Item Name="IP Checksum.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/IP Checksum.vi"/>
						<Item Name="IP Packet Info.ctl" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/IP Packet Info.ctl"/>
						<Item Name="LOC ReTx Delay.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/LOC ReTx Delay.vi"/>
						<Item Name="LOC Timeout Check.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/LOC Timeout Check.vi"/>
						<Item Name="Loss-of-Comm Monitor.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Loss-of-Comm Monitor.vi"/>
						<Item Name="Ping Reply Info.ctl" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Ping Reply Info.ctl"/>
						<Item Name="Raw Socket Ping.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Raw Socket Ping.vi"/>
						<Item Name="Recv().vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Recv().vi"/>
						<Item Name="RecvFrom().vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/RecvFrom().vi"/>
						<Item Name="Resolve IP.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Resolve IP.vi"/>
						<Item Name="Send Ping Packet.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Send Ping Packet.vi"/>
						<Item Name="Setup For Ping.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/Setup For Ping.vi"/>
						<Item Name="VerifyIpConnection.vi" Type="VI" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping/VerifyIpConnection.vi"/>
					</Item>
					<Item Name="Raw_Socket_Ping.llx" Type="Document" URL="../../../Labview Utilities/TCP-Tools/Raw_Socket_Ping.llx"/>
				</Item>
				<Item Name="AsciiLookupTable.vi" Type="VI" URL="../../../Labview Utilities/AsciiLookupTable.vi"/>
				<Item Name="Cal Interpolation.vi" Type="VI" URL="../../../Labview Utilities/Cal Interpolation.vi"/>
				<Item Name="Cal Interpolation_2.vi" Type="VI" URL="../../../Labview Utilities/Cal Interpolation_2.vi"/>
				<Item Name="Cal Interpolation_3.vi" Type="VI" URL="../../../Labview Utilities/Cal Interpolation_3.vi"/>
				<Item Name="Date Time String to Seconds_RageATE.vi" Type="VI" URL="../../../Labview Utilities/Date Time String to Seconds_RageATE.vi"/>
				<Item Name="EnterPassword.vi" Type="VI" URL="../../../Labview Utilities/EnterPassword.vi"/>
				<Item Name="FindMostRecentFile.vi" Type="VI" URL="../../../Labview Utilities/FindMostRecentFile.vi"/>
				<Item Name="FSPL_CALC.vi" Type="VI" URL="../../../Labview Utilities/FSPL_CALC.vi"/>
				<Item Name="Get Caps Lock Key State.vi" Type="VI" URL="../../../Labview Utilities/Get Caps Lock Key State.vi"/>
				<Item Name="Mixer Calc.vi" Type="VI" URL="../../../Labview Utilities/Mixer Calc.vi"/>
				<Item Name="NF_CALC.vi" Type="VI" URL="../../../Labview Utilities/NF_CALC.vi"/>
				<Item Name="Password Input VI with Key Navigation LV2012 NI Verified.vi" Type="VI" URL="../../../Labview Utilities/Password Input VI with Key Navigation LV2012 NI Verified.vi"/>
				<Item Name="PlayMediaPlayerFile.vi" Type="VI" URL="../../../Labview Utilities/PlayMediaPlayerFile.vi"/>
				<Item Name="PromptWithMessage.vi" Type="VI" URL="../../../Labview Utilities/PromptWithMessage.vi"/>
				<Item Name="RageATE_Send Email Attachment.vi" Type="VI" URL="../../../Labview Utilities/RageATE_Send Email Attachment.vi"/>
				<Item Name="RageATE_Send Email Attachment_2.vi" Type="VI" URL="../../../Labview Utilities/RageATE_Send Email Attachment_2.vi"/>
				<Item Name="RageATE_Zip File.vi" Type="VI" URL="../../../Labview Utilities/RageATE_Zip File.vi"/>
				<Item Name="relativepath.vi" Type="VI" URL="../../../Labview Utilities/relativepath.vi"/>
				<Item Name="Search 1D String Array 2012 NIVerified.vi" Type="VI" URL="../../../Labview Utilities/Search 1D String Array 2012 NIVerified.vi"/>
				<Item Name="Search 1D String Array.vi" Type="VI" URL="../../../Labview Utilities/Search 1D String Array.vi"/>
				<Item Name="SearchRepeatingArray.vi" Type="VI" URL="../../../Labview Utilities/SearchRepeatingArray.vi"/>
				<Item Name="StandAloneViDetect.vi" Type="VI" URL="../../../Labview Utilities/StandAloneViDetect.vi"/>
				<Item Name="Three Button Dialog CORE-WithTimeout.vi" Type="VI" URL="../../../Labview Utilities/Three Button Dialog CORE-WithTimeout.vi"/>
				<Item Name="FileVersionInfo.vi" Type="VI" URL="../../../Labview Utilities/FileVersionInfo.vi"/>
			</Item>
			<Item Name="Post Processors" Type="Folder">
				<Item Name="baretail.exe" Type="Document" URL="../../../Post Processors/baretail.exe"/>
				<Item Name="ConcatanateFiles.vi" Type="VI" URL="../../../Post Processors/ConcatanateFiles.vi"/>
				<Item Name="F11xx_FileMerger_V1.vi" Type="VI" URL="../../../Post Processors/F11xx_FileMerger_V1.vi"/>
				<Item Name="F11xx_FileMerger_V2.vi" Type="VI" URL="../../../Post Processors/F11xx_FileMerger_V2.vi"/>
				<Item Name="F1240_SP_FileMerger.vi" Type="VI" URL="../../../Post Processors/F1240_SP_FileMerger.vi"/>
				<Item Name="FileRenamer.vi" Type="VI" URL="../../../Post Processors/FileRenamer.vi"/>
				<Item Name="NewDVT.py" Type="Document" URL="../../../Post Processors/NewDVT.py"/>
				<Item Name="NewFinalTest.py" Type="Document" URL="../../../Post Processors/NewFinalTest.py"/>
				<Item Name="Baretail.vi" Type="VI" URL="../../../Post Processors/Baretail.vi"/>
			</Item>
			<Item Name="Utilities" Type="Folder">
				<Item Name="ADC_BinFreq_Compare.vi" Type="VI" URL="../../../Utilities/ADC_BinFreq_Compare.vi"/>
				<Item Name="Check Linear Array.vi" Type="VI" URL="../../../Utilities/Check Linear Array.vi"/>
				<Item Name="MeasHarmSelect.vi" Type="VI" URL="../../../Utilities/MeasHarmSelect.vi"/>
				<Item Name="NumEntry.vi" Type="VI" URL="../../../Utilities/NumEntry.vi"/>
				<Item Name="Ramp-Step.vi" Type="VI" URL="../../../Utilities/Ramp-Step.vi"/>
				<Item Name="Ramp.vi" Type="VI" URL="../../../Utilities/Ramp.vi"/>
				<Item Name="Ramp3.vi" Type="VI" URL="../../../Utilities/Ramp3.vi"/>
				<Item Name="SA_TRG_GET-MKR.vi" Type="VI" URL="../../../Utilities/SA_TRG_GET-MKR.vi"/>
				<Item Name="Set_Power_Ref(SA).vi" Type="VI" URL="../../../Utilities/Set_Power_Ref(SA).vi"/>
				<Item Name="USB scanner.vi" Type="VI" URL="../../../Utilities/USB scanner.vi"/>
			</Item>
			<Item Name="Zaber Gantry" Type="Folder">
				<Item Name="Labview Code from Colin" Type="Folder">
					<Item Name="Gantry" Type="Folder">
						<Item Name="__pycache__" Type="Folder">
							<Item Name="Gantry.cpython-36.pyc" Type="Document" URL="../../../Instruments/Zaber Gantry/Labview Code from Colin/Gantry/__pycache__/Gantry.cpython-36.pyc"/>
						</Item>
						<Item Name="antenna_cords-2.csv" Type="Document" URL="../../../Instruments/Zaber Gantry/Labview Code from Colin/Gantry/antenna_cords-2.csv"/>
						<Item Name="antenna_cords-3.csv" Type="Document" URL="../../../Instruments/Zaber Gantry/Labview Code from Colin/Gantry/antenna_cords-3.csv"/>
						<Item Name="antenna_cords-4.csv" Type="Document" URL="../../../Instruments/Zaber Gantry/Labview Code from Colin/Gantry/antenna_cords-4.csv"/>
						<Item Name="antenna_cords.csv" Type="Document" URL="../../../Instruments/Zaber Gantry/Labview Code from Colin/Gantry/antenna_cords.csv"/>
						<Item Name="Gantry.py" Type="Document" URL="../../../Instruments/Zaber Gantry/Labview Code from Colin/Gantry/Gantry.py"/>
						<Item Name="Gantry.vi" Type="VI" URL="../../../Instruments/Zaber Gantry/Labview Code from Colin/Gantry/Gantry.vi"/>
					</Item>
				</Item>
				<Item Name="Zaber Labview Driver" Type="Folder">
					<Item Name="Private" Type="Folder"/>
					<Item Name="Public" Type="Folder">
						<Item Name="Action-Status" Type="Folder">
							<Item Name="Force" Type="Folder">
								<Item Name="Action-Status_Force.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Action-Status/Force/Action-Status_Force.mnu"/>
							</Item>
							<Item Name="IO" Type="Folder">
								<Item Name="Action-Status_IO.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Action-Status/IO/Action-Status_IO.mnu"/>
							</Item>
							<Item Name="Lockstep" Type="Folder">
								<Item Name="Action-Status_Lockstep.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Action-Status/Lockstep/Action-Status_Lockstep.mnu"/>
							</Item>
							<Item Name="Low Level" Type="Folder">
								<Item Name="Action-Status_Low Level.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Action-Status/Low Level/Action-Status_Low Level.mnu"/>
							</Item>
							<Item Name="Streaming" Type="Folder">
								<Item Name="Action-Status_Streaming.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Action-Status/Streaming/Action-Status_Streaming.mnu"/>
							</Item>
							<Item Name="Virtual Axis" Type="Folder">
								<Item Name="Action-Status_Virtual Axis.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Action-Status/Virtual Axis/Action-Status_Virtual Axis.mnu"/>
							</Item>
							<Item Name="Action-Status.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Action-Status/Action-Status.mnu"/>
						</Item>
						<Item Name="Configure" Type="Folder">
							<Item Name="Joystick" Type="Folder">
								<Item Name="Configure_Joystick.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Configure/Joystick/Configure_Joystick.mnu"/>
							</Item>
							<Item Name="Lockstep" Type="Folder">
								<Item Name="Configure_Lockstep.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Configure/Lockstep/Configure_Lockstep.mnu"/>
							</Item>
							<Item Name="Low Level" Type="Folder">
								<Item Name="Configure_Low Level.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Configure/Low Level/Configure_Low Level.mnu"/>
							</Item>
							<Item Name="Virtual Axis" Type="Folder">
								<Item Name="Configure_Virtual Axis.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Configure/Virtual Axis/Configure_Virtual Axis.mnu"/>
							</Item>
							<Item Name="Configure.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Configure/Configure.mnu"/>
						</Item>
						<Item Name="Data" Type="Folder">
							<Item Name="IO" Type="Folder">
								<Item Name="Data_IO.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Data/IO/Data_IO.mnu"/>
							</Item>
							<Item Name="Joystick" Type="Folder">
								<Item Name="Data_Joystick.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Data/Joystick/Data_Joystick.mnu"/>
							</Item>
							<Item Name="Lockstep" Type="Folder">
								<Item Name="Data_Lockstep.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Data/Lockstep/Data_Lockstep.mnu"/>
							</Item>
							<Item Name="Low Level" Type="Folder">
								<Item Name="Data_Low Level.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Data/Low Level/Data_Low Level.mnu"/>
							</Item>
							<Item Name="Streaming" Type="Folder">
								<Item Name="Data_Streaming.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Data/Streaming/Data_Streaming.mnu"/>
							</Item>
							<Item Name="Virtual Axis" Type="Folder">
								<Item Name="Data_Virtual Axis.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Data/Virtual Axis/Data_Virtual Axis.mnu"/>
							</Item>
							<Item Name="Data.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Data/Data.mnu"/>
						</Item>
						<Item Name="Obsolete" Type="Folder"/>
						<Item Name="Utility" Type="Folder">
							<Item Name="Low Level" Type="Folder">
								<Item Name="Utility_Low Level.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Utility/Low Level/Utility_Low Level.mnu"/>
							</Item>
							<Item Name="Utility.mnu" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Public/Utility/Utility.mnu"/>
						</Item>
					</Item>
					<Item Name="RageATE-Zaber" Type="Folder">
						<Item Name="Gantry_Driver.vi" Type="VI" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/RageATE-Zaber/Gantry_Driver.vi"/>
						<Item Name="Gantry_Read-Write.vi" Type="VI" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/RageATE-Zaber/Gantry_Read-Write.vi"/>
						<Item Name="GetSystemSerialNumber.vi" Type="VI" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/RageATE-Zaber/GetSystemSerialNumber.vi"/>
						<Item Name="RageATE-LightBar.vi" Type="VI" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/RageATE-Zaber/RageATE-LightBar.vi"/>
						<Item Name="WAM_ESS.vi" Type="VI" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/RageATE-Zaber/WAM_ESS.vi"/>
						<Item Name="Zaber-ErrorCodes.csv" Type="Document" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/RageATE-Zaber/Zaber-ErrorCodes.csv"/>
					</Item>
				</Item>
			</Item>
			<Item Name="New Text Document.txt" Type="Document" URL="../../../New Text Document.txt"/>
			<Item Name="Rage ATE.pptx" Type="Document" URL="../../../Rage ATE.pptx"/>
			<Item Name="RageATE.txt" Type="Document" URL="../../../RageATE.txt"/>
			<Item Name="README.md" Type="Document" URL="../../../README.md"/>
			<Item Name="WAM_Prod.lvlps" Type="Document" URL="../../../WAM_Prod.lvlps"/>
		</Item>
		<Item Name="Support" Type="Folder">
			<Item Name="3500000_TetraProdSW" Type="Folder">
				<Item Name="AdcCalTest" Type="Folder">
					<Item Name="data" Type="Folder">
						<Item Name="TA22290101_20220728_095209.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/TA22290101_20220728_095209.txt"/>
						<Item Name="TA22290102_20220728_094354.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/TA22290102_20220728_094354.txt"/>
						<Item Name="TA22290103_20220728_094633.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/TA22290103_20220728_094633.txt"/>
						<Item Name="TA22290104_20220728_094815.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/TA22290104_20220728_094815.txt"/>
						<Item Name="TA22290105_20220728_095908.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/TA22290105_20220728_095908.txt"/>
						<Item Name="TA22290106_20220728_095715.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/TA22290106_20220728_095715.txt"/>
						<Item Name="TA22290107_20220728_095349.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/TA22290107_20220728_095349.txt"/>
						<Item Name="TA22290108_20220728_093942.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/TA22290108_20220728_093942.txt"/>
						<Item Name="TA22290109_20220728_095016.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/TA22290109_20220728_095016.txt"/>
						<Item Name="TA22290110_20220728_095538.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/TA22290110_20220728_095538.txt"/>
						<Item Name="test_20220727_184405.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/data/test_20220727_184405.txt"/>
					</Item>
					<Item Name="AdcCalTest-20220728.pptx" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/AdcCalTest-20220728.pptx"/>
					<Item Name="caladc_plot.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/caladc_plot.py"/>
					<Item Name="caladc_run.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/AdcCalTest/caladc_run.py"/>
				</Item>
				<Item Name="Assembly" Type="Folder">
					<Item Name="Assembly.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/Assembly/Assembly.py"/>
					<Item Name="Assembly.ui" Type="Document" URL="../../../Support/3500000_TetraProdSW/Assembly/Assembly.ui"/>
					<Item Name="IntegrationFile.btin" Type="Document" URL="../../../Support/3500000_TetraProdSW/Assembly/IntegrationFile.btin"/>
					<Item Name="labelPrint - special.bat" Type="Document" URL="../../../Support/3500000_TetraProdSW/Assembly/labelPrint - special.bat"/>
					<Item Name="labelPrint.bat" Type="Document" URL="../../../Support/3500000_TetraProdSW/Assembly/labelPrint.bat"/>
					<Item Name="RaGE_label2.btw" Type="Document" URL="../../../Support/3500000_TetraProdSW/Assembly/RaGE_label2.btw"/>
					<Item Name="shutter.wav" Type="Document" URL="../../../Support/3500000_TetraProdSW/Assembly/shutter.wav"/>
				</Item>
				<Item Name="BurnIn" Type="Folder">
					<Item Name="BurnIn.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/BurnIn/BurnIn.py"/>
					<Item Name="BurnIn.ui" Type="Document" URL="../../../Support/3500000_TetraProdSW/BurnIn/BurnIn.ui"/>
					<Item Name="mplwidget.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/BurnIn/mplwidget.py"/>
				</Item>
				<Item Name="FinalQc" Type="Folder">
					<Item Name="BoxContents.ui" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalQc/BoxContents.ui"/>
					<Item Name="Fail.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalQc/Fail.py"/>
					<Item Name="fails.csv" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalQc/fails.csv"/>
					<Item Name="FinalQc.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalQc/FinalQc.py"/>
					<Item Name="FinalQc.ui" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalQc/FinalQc.ui"/>
					<Item Name="Modtab.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalQc/Modtab.py"/>
					<Item Name="moduleTable.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalQc/moduleTable.py"/>
					<Item Name="test.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalQc/test.py"/>
				</Item>
				<Item Name="FinalTest" Type="Folder">
					<Item Name="ESN_to_module_SN.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalTest/ESN_to_module_SN.py"/>
					<Item Name="fixpath.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalTest/fixpath.py"/>
					<Item Name="movelog.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalTest/movelog.py"/>
					<Item Name="PostFinalTest.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalTest/PostFinalTest.py"/>
					<Item Name="PreFinalTest.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalTest/PreFinalTest.py"/>
					<Item Name="SecretScript.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalTest/SecretScript.py"/>
					<Item Name="SN_Lookup.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalTest/SN_Lookup.py"/>
					<Item Name="Verify_Employee.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/FinalTest/Verify_Employee.py"/>
				</Item>
				<Item Name="InitialTestAndConfig" Type="Folder">
					<Item Name="instructionimg" Type="Folder">
						<Item Name="image0.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image0.png"/>
						<Item Name="image1.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image1.png"/>
						<Item Name="image10.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image10.png"/>
						<Item Name="image11.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image11.png"/>
						<Item Name="image12.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image12.png"/>
						<Item Name="image13.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image13.png"/>
						<Item Name="image14.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image14.png"/>
						<Item Name="image2.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image2.png"/>
						<Item Name="image3.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image3.png"/>
						<Item Name="image4.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image4.png"/>
						<Item Name="image5.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image5.png"/>
						<Item Name="image6.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image6.png"/>
						<Item Name="image7.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image7.png"/>
						<Item Name="image8.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image8.png"/>
						<Item Name="image9.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/instructionimg/image9.png"/>
					</Item>
					<Item Name="am_top-20211221_FW6FBC9704_SW5428F86A.mcs" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/am_top-20211221_FW6FBC9704_SW5428F86A.mcs"/>
					<Item Name="am_top-20211221_FW6FBC9704_SW5428F86A0.mcs" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/am_top-20211221_FW6FBC9704_SW5428F86A0.mcs"/>
					<Item Name="Doc1.pdf" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/Doc1.pdf"/>
					<Item Name="Doc2.pdf" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/Doc2.pdf"/>
					<Item Name="fpga_log.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/fpga_log.txt"/>
					<Item Name="InitialTestAndConfig.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/InitialTestAndConfig.py"/>
					<Item Name="InitialTestAndConfig.ui" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/InitialTestAndConfig.ui"/>
					<Item Name="labels.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/labels.txt"/>
					<Item Name="PowerCycle.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/PowerCycle.py"/>
					<Item Name="prog_wam.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/prog_wam.py"/>
					<Item Name="RageLibrary.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/RageLibrary.py"/>
					<Item Name="requirements.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/requirements.txt"/>
					<Item Name="TetraPCBATestAndConfigureProcedure.pdf" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/TetraPCBATestAndConfigureProcedure.pdf"/>
					<Item Name="TetraSim.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitialTestAndConfig/TetraSim.py"/>
				</Item>
				<Item Name="InitTables" Type="Folder">
					<Item Name="InitTables.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitTables/InitTables.py"/>
					<Item Name="Technicians.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/InitTables/Technicians.txt"/>
				</Item>
				<Item Name="MRB" Type="Folder">
					<Item Name="FailGen.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/MRB/FailGen.py"/>
					<Item Name="testui.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/MRB/testui.py"/>
					<Item Name="ui_main.ui" Type="Document" URL="../../../Support/3500000_TetraProdSW/MRB/ui_main.ui"/>
					<Item Name="untitled.ui" Type="Document" URL="../../../Support/3500000_TetraProdSW/MRB/untitled.ui"/>
				</Item>
				<Item Name="release" Type="Folder">
					<Item Name="5084606_TetraPicPmic.X.production.ced45764R1.1.hex" Type="Document" URL="../../../Support/3500000_TetraProdSW/release/5084606_TetraPicPmic.X.production.ced45764R1.1.hex"/>
					<Item Name="am_top-20220801_FWA4CER2.0.3_SW7332R2.0.11.mcs" Type="Document" URL="../../../Support/3500000_TetraProdSW/release/am_top-20220801_FWA4CER2.0.3_SW7332R2.0.11.mcs"/>
					<Item Name="am_top-20220805_FWA4CER2.0.3_SW40C7R2.1.2.mcs" Type="Document" URL="../../../Support/3500000_TetraProdSW/release/am_top-20220805_FWA4CER2.0.3_SW40C7R2.1.2.mcs"/>
					<Item Name="am_top-20220808_FWA4CER2.0.3_SW18E5R2.1.3.mcs" Type="Document" URL="../../../Support/3500000_TetraProdSW/release/am_top-20220808_FWA4CER2.0.3_SW18E5R2.1.3.mcs"/>
					<Item Name="am_top-20220808_FWA4CER2.0.3_SWCAA7R2.1.4.mcs" Type="Document" URL="../../../Support/3500000_TetraProdSW/release/am_top-20220808_FWA4CER2.0.3_SWCAA7R2.1.4.mcs"/>
					<Item Name="am_top-20220817_FW3216R2.0.5_SW2CEBR2.1.14.mcs" Type="Document" URL="../../../Support/3500000_TetraProdSW/release/am_top-20220817_FW3216R2.0.5_SW2CEBR2.1.14.mcs"/>
					<Item Name="am_top-20221212_FWA587R2.2.1_SW1A16R2.2.8.mcs" Type="Document" URL="../../../Support/3500000_TetraProdSW/release/am_top-20221212_FWA587R2.2.1_SW1A16R2.2.8.mcs"/>
				</Item>
				<Item Name="tst" Type="Folder">
					<Item Name="CalcRdivRdvLimits.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/tst/CalcRdivRdvLimits.py"/>
				</Item>
				<Item Name="utils" Type="Folder">
					<Item Name="5084606_TetraPicPmic.X.production-20220710-A149R0.1.hex" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/5084606_TetraPicPmic.X.production-20220710-A149R0.1.hex"/>
					<Item Name="burninConn.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/burninConn.py"/>
					<Item Name="FIXNF.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/FIXNF.py"/>
					<Item Name="pic_revc.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/pic_revc.py"/>
					<Item Name="port_close.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/port_close.py"/>
					<Item Name="prog_e3644a.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/prog_e3644a.py"/>
					<Item Name="prog_flash.tcl" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/prog_flash.tcl"/>
					<Item Name="prog_Sorensen.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/prog_Sorensen.py"/>
					<Item Name="prog_wam.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/prog_wam.py"/>
					<Item Name="RaGE Logo.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/RaGE Logo.png"/>
					<Item Name="RaGE_Black_300ppi_1in.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/RaGE_Black_300ppi_1in.png"/>
					<Item Name="RaGE_Color_100ppi_1in.png" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/RaGE_Color_100ppi_1in.png"/>
					<Item Name="RaGE_label2.btw" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/RaGE_label2.btw"/>
					<Item Name="RageComm.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/RageComm.py"/>
					<Item Name="RageCommSiTime.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/RageCommSiTime.py"/>
					<Item Name="RageLibrary.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/RageLibrary.py"/>
					<Item Name="shutter.wav" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/shutter.wav"/>
					<Item Name="SqlFuncs.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/SqlFuncs.py"/>
					<Item Name="tempGraph.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/tempGraph.py"/>
					<Item Name="test.csv" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/test.csv"/>
					<Item Name="TestICD4Interface.X.production.hex" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/TestICD4Interface.X.production.hex"/>
					<Item Name="tetra.ini" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/tetra.ini"/>
					<Item Name="TetraSim.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/TetraSim.py"/>
					<Item Name="utils.py" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/utils.py"/>
					<Item Name="wamGood.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/utils/wamGood.txt"/>
				</Item>
				<Item Name="label.csv" Type="Document" URL="../../../Support/3500000_TetraProdSW/label.csv"/>
				<Item Name="requirements.txt" Type="Document" URL="../../../Support/3500000_TetraProdSW/requirements.txt"/>
			</Item>
			<Item Name="3500007_TetraFinalTestAnalysis" Type="Folder">
				<Item Name="__pycache__" Type="Folder">
					<Item Name="data_gatherer_class.cpython-36.pyc" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/__pycache__/data_gatherer_class.cpython-36.pyc"/>
					<Item Name="ResultsClass.cpython-36.pyc" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/__pycache__/ResultsClass.cpython-36.pyc"/>
					<Item Name="utils.cpython-36.pyc" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/__pycache__/utils.cpython-36.pyc"/>
				</Item>
				<Item Name="data_gatherer_class.py" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/data_gatherer_class.py"/>
				<Item Name="dynamicRange.py" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/dynamicRange.py"/>
				<Item Name="finalTestOutcome.py" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/finalTestOutcome.py"/>
				<Item Name="README.md" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/README.md"/>
				<Item Name="requirements.txt" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/requirements.txt"/>
				<Item Name="ResultsClass.py" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/ResultsClass.py"/>
				<Item Name="testreport.ini" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/testreport.ini"/>
				<Item Name="utils.py" Type="Document" URL="../../../Support/3500007_TetraFinalTestAnalysis/utils.py"/>
			</Item>
			<Item Name="TetraLabGUI" Type="Folder">
				<Item Name="__pycache__" Type="Folder">
					<Item Name="ant_rx_tx_map.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/ant_rx_tx_map.cpython-36.pyc"/>
					<Item Name="FpgaTableWidget.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/FpgaTableWidget.cpython-36.pyc"/>
					<Item Name="FpgaTableWidgetUI.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/FpgaTableWidgetUI.cpython-36.pyc"/>
					<Item Name="FpgaTimingWidget.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/FpgaTimingWidget.cpython-36.pyc"/>
					<Item Name="FpgaTimingWidgetUI.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/FpgaTimingWidgetUI.cpython-36.pyc"/>
					<Item Name="MainWidget.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/MainWidget.cpython-36.pyc"/>
					<Item Name="PowerSupplyWidget.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/PowerSupplyWidget.cpython-36.pyc"/>
					<Item Name="RageComm.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/RageComm.cpython-36.pyc"/>
					<Item Name="RageLibrary.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/RageLibrary.cpython-36.pyc"/>
					<Item Name="RegisterDisplay.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/RegisterDisplay.cpython-36.pyc"/>
					<Item Name="RxWidget.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/RxWidget.cpython-36.pyc"/>
					<Item Name="RxWidgetUI.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/RxWidgetUI.cpython-36.pyc"/>
					<Item Name="StateBoxWidget.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/StateBoxWidget.cpython-36.pyc"/>
					<Item Name="TetraHw.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/TetraHw.cpython-36.pyc"/>
					<Item Name="TetraLabGUISetup.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/TetraLabGUISetup.cpython-36.pyc"/>
					<Item Name="TetraRegisters.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/TetraRegisters.cpython-36.pyc"/>
					<Item Name="TetraSim.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/TetraSim.cpython-36.pyc"/>
					<Item Name="TxAdarAddressMap.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/TxAdarAddressMap.cpython-36.pyc"/>
					<Item Name="TxWidget.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/TxWidget.cpython-36.pyc"/>
					<Item Name="TxWidgetUI.cpython-36.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/TxWidgetUI.cpython-36.pyc"/>
					<Item Name="ant_rx_tx_map.cpython-39.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/ant_rx_tx_map.cpython-39.pyc"/>
					<Item Name="RageComm.cpython-313.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/RageComm.cpython-313.pyc"/>
					<Item Name="RageComm.cpython-39.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/RageComm.cpython-39.pyc"/>
					<Item Name="TetraRegisters.cpython-39.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/TetraRegisters.cpython-39.pyc"/>
					<Item Name="TetraSim.cpython-39.pyc" Type="Document" URL="../../../Support/TetraLabGUI/__pycache__/TetraSim.cpython-39.pyc"/>
				</Item>
				<Item Name="ant_rx_tx_map.py" Type="Document" URL="../../../Support/TetraLabGUI/ant_rx_tx_map.py"/>
				<Item Name="bandpower.ini" Type="Document" URL="../../../Support/TetraLabGUI/bandpower.ini"/>
				<Item Name="BPClient.py" Type="Document" URL="../../../Support/TetraLabGUI/BPClient.py"/>
				<Item Name="BpClient_Avg.py" Type="Document" URL="../../../Support/TetraLabGUI/BpClient_Avg.py"/>
				<Item Name="outputhex9_13.txt" Type="Document" URL="../../../Support/TetraLabGUI/outputhex9_13.txt"/>
				<Item Name="RageComm.py" Type="Document" URL="../../../Support/TetraLabGUI/RageComm.py"/>
				<Item Name="RageLibrary.py" Type="Document" URL="../../../Support/TetraLabGUI/RageLibrary.py"/>
				<Item Name="ReadAdc.py" Type="Document" URL="../../../Support/TetraLabGUI/ReadAdc.py"/>
				<Item Name="ReadADCClient.py" Type="Document" URL="../../../Support/TetraLabGUI/ReadADCClient.py"/>
				<Item Name="TetraRegisters.py" Type="Document" URL="../../../Support/TetraLabGUI/TetraRegisters.py"/>
				<Item Name="TetraSim.py" Type="Document" URL="../../../Support/TetraLabGUI/TetraSim.py"/>
				<Item Name="AmInit.py" Type="Document" URL="../../../Support/TetraLabGUI/AmInit.py"/>
				<Item Name="dllNew.py" Type="Document" URL="../../../Support/TetraLabGUI/dllNew.py"/>
				<Item Name="dllwrapper.py" Type="Document" URL="../../../Support/TetraLabGUI/dllwrapper.py"/>
				<Item Name="DynamicModeInit.py" Type="Document" URL="../../../Support/TetraLabGUI/DynamicModeInit.py"/>
				<Item Name="FieldTestClient.dll" Type="Document" URL="../../../Support/TetraLabGUI/FieldTestClient.dll"/>
				<Item Name="ResetandArmRFSM.py" Type="Document" URL="../../../Support/TetraLabGUI/ResetandArmRFSM.py"/>
			</Item>
			<Item Name="FieldTestApp" Type="Folder">
				<Item Name="cmdGetFpgaVer.txt" Type="Document" URL="../../../Support/FieldTestApp/cmdGetFpgaVer.txt"/>
				<Item Name="dfltlog.txt" Type="Document" URL="../../../Support/FieldTestApp/dfltlog.txt"/>
				<Item Name="dfltlog_older.txt" Type="Document" URL="../../../Support/FieldTestApp/dfltlog_older.txt"/>
				<Item Name="DmaTable_AllAms_2Demods.txt" Type="Document" URL="../../../Support/FieldTestApp/DmaTable_AllAms_2Demods.txt"/>
				<Item Name="DmaTable_Am1Only_2Demods.txt" Type="Document" URL="../../../Support/FieldTestApp/DmaTable_Am1Only_2Demods.txt"/>
				<Item Name="DmaTable_AutoGeneratedFromAmCombinedTable.txt" Type="Document" URL="../../../Support/FieldTestApp/DmaTable_AutoGeneratedFromAmCombinedTable.txt"/>
				<Item Name="DS90UB925Q_AM_Registers_Full.txt" Type="Document" URL="../../../Support/FieldTestApp/DS90UB925Q_AM_Registers_Full.txt"/>
				<Item Name="DS90UB925Q_AM_Registers_Min.txt" Type="Document" URL="../../../Support/FieldTestApp/DS90UB925Q_AM_Registers_Min.txt"/>
				<Item Name="DS90UB925Q_V3ISU_Registers_Full.txt" Type="Document" URL="../../../Support/FieldTestApp/DS90UB925Q_V3ISU_Registers_Full.txt"/>
				<Item Name="DS90UB925Q_V3ISU_Registers_Min.txt" Type="Document" URL="../../../Support/FieldTestApp/DS90UB925Q_V3ISU_Registers_Min.txt"/>
				<Item Name="DS90UB926Q_RFSM_Registers_Full.txt" Type="Document" URL="../../../Support/FieldTestApp/DS90UB926Q_RFSM_Registers_Full.txt"/>
				<Item Name="DS90UB926Q_RFSM_Registers_Min.txt" Type="Document" URL="../../../Support/FieldTestApp/DS90UB926Q_RFSM_Registers_Min.txt"/>
				<Item Name="DS90UB928Q_V3ISU_Registers_Full.txt" Type="Document" URL="../../../Support/FieldTestApp/DS90UB928Q_V3ISU_Registers_Full.txt"/>
				<Item Name="DS90UB928Q_V3ISU_Registers_Min.txt" Type="Document" URL="../../../Support/FieldTestApp/DS90UB928Q_V3ISU_Registers_Min.txt"/>
				<Item Name="FieldTest.exe" Type="Document" URL="../../../Support/FieldTestApp/FieldTest.exe"/>
				<Item Name="libfftw3-3.dll" Type="Document" URL="../../../Support/FieldTestApp/libfftw3-3.dll"/>
				<Item Name="RegisterBreakoutForTreeControl_DS90UB925Q.txt" Type="Document" URL="../../../Support/FieldTestApp/RegisterBreakoutForTreeControl_DS90UB925Q.txt"/>
				<Item Name="RegisterBreakoutForTreeControl_DS90UB926Q.txt" Type="Document" URL="../../../Support/FieldTestApp/RegisterBreakoutForTreeControl_DS90UB926Q.txt"/>
				<Item Name="RegisterBreakoutForTreeControl_DS90UB928Q.txt" Type="Document" URL="../../../Support/FieldTestApp/RegisterBreakoutForTreeControl_DS90UB928Q.txt"/>
				<Item Name="RegisterBreakoutForTreeControl_RFSM.txt" Type="Document" URL="../../../Support/FieldTestApp/RegisterBreakoutForTreeControl_RFSM.txt"/>
				<Item Name="RegisterBreakoutForTreeControl_V3ISU_0011.txt" Type="Document" URL="../../../Support/FieldTestApp/RegisterBreakoutForTreeControl_V3ISU_0011.txt"/>
				<Item Name="RegisterBreakoutForTreeControl_V3ISUTesterBrd.txt" Type="Document" URL="../../../Support/FieldTestApp/RegisterBreakoutForTreeControl_V3ISUTesterBrd.txt"/>
				<Item Name="RFSM_Registers_WithRunningStart.txt" Type="Document" URL="../../../Support/FieldTestApp/RFSM_Registers_WithRunningStart.txt"/>
				<Item Name="RFSM_Registers_WithRunningStart_Am1Only.txt" Type="Document" URL="../../../Support/FieldTestApp/RFSM_Registers_WithRunningStart_Am1Only.txt"/>
				<Item Name="testConfig.scn" Type="Document" URL="../../../Support/FieldTestApp/testConfig.scn"/>
				<Item Name="testConfig_LoadBoard.scn" Type="Document" URL="../../../Support/FieldTestApp/testConfig_LoadBoard.scn"/>
				<Item Name="testConfig_RfsmOnly.scn" Type="Document" URL="../../../Support/FieldTestApp/testConfig_RfsmOnly.scn"/>
				<Item Name="v3isu0_registers_0000.txt" Type="Document" URL="../../../Support/FieldTestApp/v3isu0_registers_0000.txt"/>
				<Item Name="v3isu0_registers_0010.txt" Type="Document" URL="../../../Support/FieldTestApp/v3isu0_registers_0010.txt"/>
				<Item Name="v3isu0_registers_0010_Am1Only.txt" Type="Document" URL="../../../Support/FieldTestApp/v3isu0_registers_0010_Am1Only.txt"/>
				<Item Name="v3isu0_registers_0011.txt" Type="Document" URL="../../../Support/FieldTestApp/v3isu0_registers_0011.txt"/>
				<Item Name="v3isu0_registers_0011_Am1Only.txt" Type="Document" URL="../../../Support/FieldTestApp/v3isu0_registers_0011_Am1Only.txt"/>
				<Item Name="v3isu1_registers_0010.txt" Type="Document" URL="../../../Support/FieldTestApp/v3isu1_registers_0010.txt"/>
				<Item Name="v3isu1_registers_0010_Am1Only.txt" Type="Document" URL="../../../Support/FieldTestApp/v3isu1_registers_0010_Am1Only.txt"/>
				<Item Name="v3isu1_registers_0011.txt" Type="Document" URL="../../../Support/FieldTestApp/v3isu1_registers_0011.txt"/>
				<Item Name="v3isu1_registers_0011_Am1Only.txt" Type="Document" URL="../../../Support/FieldTestApp/v3isu1_registers_0011_Am1Only.txt"/>
			</Item>
			<Item Name="Tests Path_Eng.ini" Type="Document" URL="../../../Support/Tests Path_Eng.ini"/>
			<Item Name="Tests Path_Prod.ini" Type="Document" URL="../../../Support/Tests Path_Prod.ini"/>
			<Item Name="Test Count.ini" Type="Document" URL="../../../Support/Test Count.ini"/>
			<Item Name="imon_revc_limits.ini" Type="Document" URL="../../../Support/imon_revc_limits.ini"/>
			<Item Name="imon_revLc_limits.ini" Type="Document" URL="../../../Support/imon_revLc_limits.ini"/>
		</Item>
		<Item Name="WAM-PROD_Sequencer.vi" Type="VI" URL="../WAM-PROD_Sequencer.vi"/>
		<Item Name="Load and Save Controls.vi" Type="VI" URL="../../../Labview Utilities/Load and Save Controls_LV2009/Load and Save Controls.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Add File to Zip.vi" Type="VI" URL="/&lt;vilib&gt;/zip/Add File to Zip.vi"/>
				<Item Name="Application Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Application Directory.vi"/>
				<Item Name="Assert Block Data Type.vim" Type="VI" URL="/&lt;vilib&gt;/Utility/TypeAssert/Assert Block Data Type.vim"/>
				<Item Name="Beep.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/Beep.vi"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="Close Registry Key.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Close Registry Key.vi"/>
				<Item Name="Close Zip File.vi" Type="VI" URL="/&lt;vilib&gt;/zip/Close Zip File.vi"/>
				<Item Name="Compare Two Paths.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Compare Two Paths.vi"/>
				<Item Name="compatCalcOffset.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatCalcOffset.vi"/>
				<Item Name="compatFileDialog.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatFileDialog.vi"/>
				<Item Name="compatOpenFileOperation.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatOpenFileOperation.vi"/>
				<Item Name="compatReadText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatReadText.vi"/>
				<Item Name="compatWriteText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatWriteText.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="Dynamic To Waveform Array.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/Dynamic To Waveform Array.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="ex_BuildTextVarProps.ctl" Type="VI" URL="/&lt;vilib&gt;/express/express output/BuildTextBlock.llb/ex_BuildTextVarProps.ctl"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="ex_GetAllExpressAttribsPlus.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/ex_GetAllExpressAttribsPlus.vi"/>
				<Item Name="ex_Modify Signal Name.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_Modify Signal Name.vi"/>
				<Item Name="ex_Modify Signals Names.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_Modify Signals Names.vi"/>
				<Item Name="ex_SetAllExpressAttribs.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/ex_SetAllExpressAttribs.vi"/>
				<Item Name="ex_WaveformAttribs.ctl" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/ex_WaveformAttribs.ctl"/>
				<Item Name="ex_WaveformAttribsPlus.ctl" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/ex_WaveformAttribsPlus.ctl"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="Generate Temporary File Path.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Generate Temporary File Path.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="High Resolution Polling Wait.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/High Resolution Polling Wait.vi"/>
				<Item Name="High Resolution Relative Seconds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/High Resolution Relative Seconds.vi"/>
				<Item Name="Is Path and Not Empty.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Is Path and Not Empty.vi"/>
				<Item Name="Is Value Changed.vim" Type="VI" URL="/&lt;vilib&gt;/Utility/Is Value Changed.vim"/>
				<Item Name="LabVIEWSMTPClient.lvlib" Type="Library" URL="/&lt;vilib&gt;/smtpClient/LabVIEWSMTPClient.lvlib"/>
				<Item Name="List Directory and LLBs.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/List Directory and LLBs.vi"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="LVDateTimeRec.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVDateTimeRec.ctl"/>
				<Item Name="LVPointTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVPointTypeDef.ctl"/>
				<Item Name="LVPositionTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVPositionTypeDef.ctl"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="Move t0 to the end.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/Move t0 to the end.vi"/>
				<Item Name="New Zip File.vi" Type="VI" URL="/&lt;vilib&gt;/zip/New Zip File.vi"/>
				<Item Name="NI_AALBase.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALBase.lvlib"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_Gmath.lvlib" Type="Library" URL="/&lt;vilib&gt;/gmath/NI_Gmath.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Open File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Open File+.vi"/>
				<Item Name="Open Registry Key.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Open Registry Key.vi"/>
				<Item Name="Open_Create_Replace File.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/Open_Create_Replace File.vi"/>
				<Item Name="Path To Command Line String.vi" Type="VI" URL="/&lt;vilib&gt;/AdvancedString/Path To Command Line String.vi"/>
				<Item Name="PathToUNIXPathString.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFURL.llb/PathToUNIXPathString.vi"/>
				<Item Name="Read Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Read Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (I64).vi"/>
				<Item Name="Read Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (string).vi"/>
				<Item Name="Read Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet.vi"/>
				<Item Name="Read File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read File+ (string).vi"/>
				<Item Name="Read From Spreadsheet File (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File (DBL).vi"/>
				<Item Name="Read From Spreadsheet File (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File (I64).vi"/>
				<Item Name="Read From Spreadsheet File (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File (string).vi"/>
				<Item Name="Read From Spreadsheet File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File.vi"/>
				<Item Name="Read Lines From File (with error IO).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Lines From File (with error IO).vi"/>
				<Item Name="Read Lines From File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Lines From File.vi"/>
				<Item Name="Read Registry Value DWORD.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value DWORD.vi"/>
				<Item Name="Read Registry Value Simple STR.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple STR.vi"/>
				<Item Name="Read Registry Value Simple U32.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple U32.vi"/>
				<Item Name="Read Registry Value Simple.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple.vi"/>
				<Item Name="Read Registry Value STR.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value STR.vi"/>
				<Item Name="Read Registry Value.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value.vi"/>
				<Item Name="Recursive File List.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Recursive File List.vi"/>
				<Item Name="Registry Handle Master.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry Handle Master.vi"/>
				<Item Name="Registry refnum.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry refnum.ctl"/>
				<Item Name="Registry RtKey.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry RtKey.ctl"/>
				<Item Name="Registry SAM.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry SAM.ctl"/>
				<Item Name="Registry Simplify Data Type.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry Simplify Data Type.vi"/>
				<Item Name="Registry View.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry View.ctl"/>
				<Item Name="Registry WinErr-LVErr.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry WinErr-LVErr.vi"/>
				<Item Name="Relative Path To Platform Independent String.vi" Type="VI" URL="/&lt;vilib&gt;/AdvancedString/Relative Path To Platform Independent String.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Select Event Type.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/Select Event Type.ctl"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Set Busy.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Busy.vi"/>
				<Item Name="Set Cursor (Cursor ID).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Cursor (Cursor ID).vi"/>
				<Item Name="Set Cursor (Icon Pict).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Cursor (Icon Pict).vi"/>
				<Item Name="Set Cursor.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Cursor.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="Sort 2D Array - Pop Stack.vi" Type="VI" URL="/&lt;vilib&gt;/Array/Sort 2D Array - Pop Stack.vi"/>
				<Item Name="Sort 2D Array - Push Stack.vi" Type="VI" URL="/&lt;vilib&gt;/Array/Sort 2D Array - Push Stack.vi"/>
				<Item Name="Sort 2D Array.vim" Type="VI" URL="/&lt;vilib&gt;/Array/Sort 2D Array.vim"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="StatisticsType.ctl" Type="VI" URL="/&lt;vilib&gt;/express/express shared/StatisticsType.ctl"/>
				<Item Name="STR_ASCII-Unicode.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/STR_ASCII-Unicode.vi"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
				<Item Name="subFile Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/FileDialogBlock.llb/subFile Dialog.vi"/>
				<Item Name="subHistogram.vi" Type="VI" URL="/&lt;vilib&gt;/express/express analysis/HistogramBlock.llb/subHistogram.vi"/>
				<Item Name="subStatistics.vi" Type="VI" URL="/&lt;vilib&gt;/express/express analysis/StatisticsBlock.llb/subStatistics.vi"/>
				<Item Name="subTimeDelay.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/TimeDelayBlock.llb/subTimeDelay.vi"/>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Unset Busy.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Unset Busy.vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="VISA Flush IO Buffer Mask.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Flush IO Buffer Mask.ctl"/>
				<Item Name="VISA GPIB Control REN Mode.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA GPIB Control REN Mode.ctl"/>
				<Item Name="Waveform Array To Dynamic.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/Waveform Array To Dynamic.vi"/>
				<Item Name="Waveform Min Max.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/WDTOps.llb/Waveform Min Max.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Write Characters To File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Characters To File.vi"/>
				<Item Name="Write Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Write Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (I64).vi"/>
				<Item Name="Write Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (string).vi"/>
				<Item Name="Write Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet.vi"/>
				<Item Name="Write File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write File+ (string).vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
				<Item Name="Write To Spreadsheet File (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (DBL).vi"/>
				<Item Name="Write To Spreadsheet File (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (I64).vi"/>
				<Item Name="Write To Spreadsheet File (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (string).vi"/>
				<Item Name="Write To Spreadsheet File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File.vi"/>
				<Item Name="BuildErrorSource.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/BuildErrorSource.vi"/>
				<Item Name="FixedFileInfo_Struct.ctl" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/FixedFileInfo_Struct.ctl"/>
				<Item Name="MoveMemory.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/MoveMemory.vi"/>
				<Item Name="VerQueryValue.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/VerQueryValue.vi"/>
				<Item Name="GetFileVersionInfo.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/GetFileVersionInfo.vi"/>
				<Item Name="GetFileVersionInfoSize.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/GetFileVersionInfoSize.vi"/>
				<Item Name="FileVersionInformation.ctl" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/FileVersionInformation.ctl"/>
				<Item Name="8.6CompatibleGlobalVar.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/config.llb/8.6CompatibleGlobalVar.vi"/>
				<Item Name="NI_LVConfig.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/config.llb/NI_LVConfig.lvlib"/>
				<Item Name="Dflt Data Dir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Dflt Data Dir.vi"/>
				<Item Name="FormatTime String.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/ElapsedTimeBlock.llb/FormatTime String.vi"/>
				<Item Name="subElapsedTime.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/ElapsedTimeBlock.llb/subElapsedTime.vi"/>
			</Item>
			<Item Name="Advapi32.dll" Type="Document" URL="Advapi32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="CVIRTE.DLL" Type="Document" URL="CVIRTE.DLL">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="kernel32.dll" Type="Document" URL="kernel32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="libsystem_kernel.dylib" Type="Document" URL="/usr/lib/system/libsystem_kernel.dylib"/>
			<Item Name="lvanlys.dll" Type="Document" URL="/&lt;resource&gt;/lvanlys.dll"/>
			<Item Name="mscorlib" Type="VI" URL="mscorlib">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nilvaiu.dll" Type="Document" URL="nilvaiu.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="psapi.dll" Type="Document" URL="psapi.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Serial - ASCII Characters.ctl" Type="VI" URL="../../../../Program Files (x86)/National Instruments/LabVIEW 2018/examples/Instrument IO/Serial/support/Serial - ASCII Characters.ctl"/>
			<Item Name="Serial - Settings.ctl" Type="VI" URL="../../../../Program Files (x86)/National Instruments/LabVIEW 2018/examples/Instrument IO/Serial/support/Serial - Settings.ctl"/>
			<Item Name="Serial - XON-XOFF Characters.ctl" Type="VI" URL="../../../../Program Files (x86)/National Instruments/LabVIEW 2018/examples/Instrument IO/Serial/support/Serial - XON-XOFF Characters.ctl"/>
			<Item Name="System" Type="VI" URL="System">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="System.Management" Type="Document" URL="System.Management">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="System.Windows.Forms" Type="Document" URL="System.Windows.Forms">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="ws2_32.dll" Type="Document" URL="ws2_32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="version.dll" Type="Document" URL="version.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="RWC_Actions.ctl" Type="VI" URL="../../../Labview Utilities/Load and Save Controls_LV2009/RWC_Actions.ctl"/>
			<Item Name="Read and Write Controls to Config File.vi" Type="VI" URL="../../../Labview Utilities/Load and Save Controls_LV2009/Read and Write Controls to Config File.vi"/>
			<Item Name="Read and Write Controls to Automatic Config File.vi" Type="VI" URL="../../../Labview Utilities/Load and Save Controls_LV2009/Read and Write Controls to Automatic Config File.vi"/>
			<Item Name="SelectTester-PopUp.vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/SelectTester-PopUp.vi"/>
			<Item Name="GetRxPower(LC).vi" Type="VI" URL="../../../Automated Tests/Tetra WAM/Utilities/GetRxPower(LC).vi"/>
			<Item Name="PingTestBoard(LC).vi" Type="VI" URL="../../../Automated Tests/Tetra_Bounce/PingTestBoard(LC).vi"/>
			<Item Name="ParseBounceData.vi" Type="VI" URL="../../../Automated Tests/Tetra_Bounce/ParseBounceData.vi"/>
			<Item Name="VcoTest.vi" Type="VI" URL="../../../Automated Tests/Tetra_Bounce/VcoTest.vi"/>
			<Item Name="ConnectToISU.vi" Type="VI" URL="../../../Automated Tests/Tetra_Bounce/ConnectToISU.vi"/>
			<Item Name="ConnectFieldTestServer.vi" Type="VI" URL="../../../Automated Tests/Tetra_Bounce/ConnectFieldTestServer.vi"/>
			<Item Name="Bounce(LC).vi" Type="VI" URL="../../../Automated Tests/Tetra_Bounce/Bounce(LC).vi"/>
			<Item Name="Agilent N6700 Series.lvlib" Type="Library" URL="../../../Instruments/Keysight N6700/Agilent N6700 Series/Agilent N6700 Series.lvlib"/>
			<Item Name="PM9 Set Temp and Wait.vi" Type="VI" URL="../../../Instruments/Ess Temp Plate/LabView Driver/EthTCPModbus/Public/PM9 Set Temp and Wait.vi"/>
			<Item Name="Watbus.dll" Type="Document" URL="../../../Instruments/Ess Temp Plate/LabView Driver/Public/Watbus.dll"/>
			<Item Name="PM9_TCP_MODE.vi" Type="VI" URL="../../../Instruments/Ess Temp Plate/LabView Driver/EthTCPModbus/Private/PM9_TCP_MODE.vi"/>
			<Item Name="PM9_TCP_DEG-UNITS.vi" Type="VI" URL="../../../Instruments/Ess Temp Plate/LabView Driver/EthTCPModbus/Private/PM9_TCP_DEG-UNITS.vi"/>
			<Item Name="PM9_TCP_REMOTE-SET-SETPOINT.vi" Type="VI" URL="../../../Instruments/Ess Temp Plate/LabView Driver/EthTCPModbus/Private/PM9_TCP_REMOTE-SET-SETPOINT.vi"/>
			<Item Name="PM9_TCP_READ-TEMP.vi" Type="VI" URL="../../../Instruments/Ess Temp Plate/LabView Driver/EthTCPModbus/Private/PM9_TCP_READ-TEMP.vi"/>
			<Item Name="INST_PS_SET_VOLTAGE_LEVEL_4.0.0.vi" Type="VI" URL="../../../Instruments/Power Supply/INST_PS_SET_VOLTAGE_LEVEL_4.0.0.vi"/>
			<Item Name="VISA_OPC.vi" Type="VI" URL="../../../Instruments/VISA_OPC.vi"/>
			<Item Name="INST_PS_MEAS_3.0.0.vi" Type="VI" URL="../../../Instruments/Power Supply/INST_PS_MEAS_3.0.0.vi"/>
			<Item Name="RfSwitch_WAM_ATE.vi" Type="VI" URL="../../../Instruments/Keysight 11713 Switch/RfSwitch_WAM_ATE.vi"/>
			<Item Name="PS_SETUP_V-I-EN.vi" Type="VI" URL="../../../Instruments/Power Supply/PS_SETUP_V-I-EN.vi"/>
			<Item Name="INST_PS_CONFIG_OUTPUT.vi" Type="VI" URL="../../../Instruments/Power Supply/INST_PS_CONFIG_OUTPUT.vi"/>
			<Item Name="INST_PS_SET_CURRENT_LEVEL_4.0.0.vi" Type="VI" URL="../../../Instruments/Power Supply/INST_PS_SET_CURRENT_LEVEL_4.0.0.vi"/>
			<Item Name="PM9_TCP_READ-SN.vi" Type="VI" URL="../../../Instruments/Ess Temp Plate/LabView Driver/EthTCPModbus/Private/PM9_TCP_READ-SN.vi"/>
			<Item Name="PM9_TCP_READ-DEV-STATUS.vi" Type="VI" URL="../../../Instruments/Ess Temp Plate/LabView Driver/EthTCPModbus/Private/PM9_TCP_READ-DEV-STATUS.vi"/>
			<Item Name="VISA_RESET-CLS.vi" Type="VI" URL="../../../Instruments/VISA_RESET-CLS.vi"/>
			<Item Name="VISA_IDN.vi" Type="VI" URL="../../../Instruments/VISA_IDN.vi"/>
			<Item Name="RageEquipCal_Lookup.vi" Type="VI" URL="../../../Instruments/RageEquipCal_Lookup.vi"/>
			<Item Name="11713_IDN.vi" Type="VI" URL="../../../Instruments/11713_IDN.vi"/>
			<Item Name="VISA_WRITE_2.vi" Type="VI" URL="../../../Instruments/VISA_WRITE_2.vi"/>
			<Item Name="Keysight PNA Series.lvlib" Type="Library" URL="../../../Instruments/Agilent N5232A PNA-L/Labview Driver/Keysight PNA Series/Keysight PNA Series.lvlib"/>
			<Item Name="Agilent ENA Series.lvlib" Type="Library" URL="../../../Instruments/PNA/lib functions/Agilent ENA Series.lvlib"/>
			<Item Name="PNA_MAIN_RF_STATE.vi" Type="VI" URL="../../../Instruments/PNA/PNA_MAIN_RF_STATE.vi"/>
			<Item Name="VSG_SET_RF_STATE_1.00.vi" Type="VI" URL="../../../Instruments/Signal Generator/VSG_SET_RF_STATE_1.00.vi"/>
			<Item Name="VSG_SET-GET_AMPL_3.00.vi" Type="VI" URL="../../../Instruments/Signal Generator/VSG_SET-GET_AMPL_3.00.vi"/>
			<Item Name="VISA_CLS.vi" Type="VI" URL="../../../Instruments/VISA_CLS.vi"/>
			<Item Name="VSG_SET-GET_CW_1.00.vi" Type="VI" URL="../../../Instruments/Signal Generator/VSG_SET-GET_CW_1.00.vi"/>
			<Item Name="PNA-L_SET-CWFREQ.vi" Type="VI" URL="../../../Instruments/PNA/PNA-L_SET-CWFREQ.vi"/>
			<Item Name="Agilent PSG MXG Series.lvlib" Type="Library" URL="../../../Instruments/Agilent PSG MXG Series/Agilent PSG MXG Series.lvlib"/>
			<Item Name="Flatness_PreSet.vi" Type="VI" URL="../../../Instruments/Agilent PSG MXG Series/Public/User Flatness/Flatness_PreSet.vi"/>
			<Item Name="Flatness-SetupFrequency.vi" Type="VI" URL="../../../Instruments/Agilent PSG MXG Series/Public/User Flatness/Flatness-SetupFrequency.vi"/>
			<Item Name="Flatness_Load-CalFromStep.vi" Type="VI" URL="../../../Instruments/Agilent PSG MXG Series/Public/User Flatness/Flatness_Load-CalFromStep.vi"/>
			<Item Name="Flatness_Load-Pairs.vi" Type="VI" URL="../../../Instruments/Agilent PSG MXG Series/Public/User Flatness/Flatness_Load-Pairs.vi"/>
			<Item Name="Flatness_ON-OFF.vi" Type="VI" URL="../../../Instruments/Agilent PSG MXG Series/Public/User Flatness/Flatness_ON-OFF.vi"/>
			<Item Name="PS_MEASURE_V-I_Ary.vi" Type="VI" URL="../../../Instruments/Power Supply/PS_MEASURE_V-I_Ary.vi"/>
			<Item Name="Configure Marker_RageATE.vi" Type="VI" URL="../../../Instruments/Agilent N5232A PNA-L/Labview Driver/Keysight PNA Series/Public/Configure/Configure Marker_RageATE.vi"/>
			<Item Name="PNA-L_MKR_RageATE.vi" Type="VI" URL="../../../Instruments/Agilent N5232A PNA-L/Labview Driver/Keysight PNA Series/Public/Data/PNA-L_MKR_RageATE.vi"/>
			<Item Name="SA_SET_CF.vi" Type="VI" URL="../../../Instruments/Spectrum Analyzer/SA_SET_CF.vi"/>
			<Item Name="SA_AVG.vi" Type="VI" URL="../../../Instruments/Spectrum Analyzer/SA_AVG.vi"/>
			<Item Name="SA_GET_MARKER.vi" Type="VI" URL="../../../Instruments/Spectrum Analyzer/SA_GET_MARKER.vi"/>
			<Item Name="GLOBAL CENTER FREQ.vi" Type="VI" URL="../../../Instruments/Keysight N9010A/GLOBAL CENTER FREQ.vi"/>
			<Item Name="AVG_TRACE.vi" Type="VI" URL="../../../Instruments/Keysight N9010A/AVG_TRACE.vi"/>
			<Item Name="GET_MARKER.vi" Type="VI" URL="../../../Instruments/Keysight N9010A/GET_MARKER.vi"/>
			<Item Name="Instrument Mode.vi" Type="VI" URL="../../../Instruments/Keysight N9010A/Instrument Mode.vi"/>
			<Item Name="EXA_RCL_STATE.vi" Type="VI" URL="../../../Instruments/Keysight N9010A/EXA_RCL_STATE.vi"/>
			<Item Name="VISA_WRITE-READ.vi" Type="VI" URL="../../../Instruments/VISA_WRITE-READ.vi"/>
			<Item Name="FREQ_SPAN.vi" Type="VI" URL="../../../Instruments/Keysight N9010A/FREQ_SPAN.vi"/>
			<Item Name="SA_RBW.vi" Type="VI" URL="../../../Instruments/Keysight N9010A/SA_RBW.vi"/>
			<Item Name="REF_LEV.vi" Type="VI" URL="../../../Instruments/Keysight N9010A/REF_LEV.vi"/>
			<Item Name="SA_ATT.vi" Type="VI" URL="../../../Instruments/Keysight N9010A/SA_ATT.vi"/>
			<Item Name="SWEEP_CONT.vi" Type="VI" URL="../../../Instruments/Keysight N9010A/SWEEP_CONT.vi"/>
			<Item Name="N5232-PNA_ExecuteShortcut.vi" Type="VI" URL="../../../Instruments/Agilent N5232A PNA-L/Labview Driver/RageATE-PNA/N5232-PNA_ExecuteShortcut.vi"/>
			<Item Name="GetSpData.vi" Type="VI" URL="../../../Instruments/Agilent N5232A PNA-L/Labview Driver/RageATE-PNA/GetSpData.vi"/>
			<Item Name="N5232-PNA_ReadChanTrigger.vi" Type="VI" URL="../../../Instruments/Agilent N5232A PNA-L/Labview Driver/RageATE-PNA/N5232-PNA_ReadChanTrigger.vi"/>
			<Item Name="N5232-ReadAverageMode.vi" Type="VI" URL="../../../Instruments/Agilent N5232A PNA-L/Labview Driver/RageATE-PNA/N5232-ReadAverageMode.vi"/>
			<Item Name="GetFreq.vi" Type="VI" URL="../../../Instruments/Agilent N5232A PNA-L/Labview Driver/RageATE-PNA/GetFreq.vi"/>
			<Item Name="SA_SET_REFSRC.vi" Type="VI" URL="../../../Instruments/Spectrum Analyzer/SA_SET_REFSRC.vi"/>
			<Item Name="SA_PREAMP.vi" Type="VI" URL="../../../Instruments/Spectrum Analyzer/SA_PREAMP.vi"/>
			<Item Name="Agilent U2000 Series.lvlib" Type="Library" URL="../../../Instruments/Keysight U2022 Power Sensor/Agilent U2000 Series/Agilent U2000 Series.lvlib"/>
			<Item Name="Visa_Reset_Clear.vi" Type="VI" URL="../../../Instruments/VISA/Visa_Reset_Clear.vi"/>
			<Item Name="SIGGEN_AMPL.vi" Type="VI" URL="../../../Instruments/Signal Generator/SIGGEN_AMPL.vi"/>
			<Item Name="VISA_LCL.vi" Type="VI" URL="../../../Instruments/VISA_LCL.vi"/>
			<Item Name="Send Trigger and Wait for OPC.vi" Type="VI" URL="../../../Instruments/Spectrum Analyzer/Send Trigger and Wait for OPC.vi"/>
			<Item Name="PNA-X.lvlib" Type="Library" URL="../../../Instruments/PNA-X/PNA-X.lvlib"/>
			<Item Name="PNA-X_GetFileInfo.vi" Type="VI" URL="../../../Instruments/PNA-X/RageATE-PNAX/PNA-X_GetFileInfo.vi"/>
			<Item Name="MMEM_DAT-FLAG.vi" Type="VI" URL="../../../Instruments/PNA-X/RageATE-PNAX/MMEM_DAT-FLAG.vi"/>
			<Item Name="SYST_DATE-TIME.vi" Type="VI" URL="../../../Instruments/PNA-X/Low Level/System/SYST_DATE-TIME.vi"/>
			<Item Name="PNA_Parse_Time-Date.vi" Type="VI" URL="../../../Instruments/PNA-X/RageATE-PNAX/PNA_Parse_Time-Date.vi"/>
			<Item Name="N6700_OUTPUT_COUPLE.vi" Type="VI" URL="../../../Instruments/Keysight N6700/N6700_OUTPUT_COUPLE.vi"/>
			<Item Name="INST_PS_GET_VOLT-CURR-SET_LEVEL.vi" Type="VI" URL="../../../Instruments/Power Supply/INST_PS_GET_VOLT-CURR-SET_LEVEL.vi"/>
			<Item Name="Zaber A Series.lvlib" Type="Library" URL="../../../Instruments/Zaber Gantry/Zaber Labview Driver/Zaber A Series.lvlib"/>
			<Item Name="PM9_TCP_MODE.vi" Type="VI" URL="../../../../RageATE/Instruments/Ess Temp Plate/LabView Driver/EthTCPModbus/Private/PM9_TCP_MODE.vi"/>
			<Item Name="Keysight PNA Series.lvlib" Type="Library" URL="../../../../RageATE/Instruments/Agilent N5232A PNA-L/Labview Driver/Keysight PNA Series/Keysight PNA Series.lvlib"/>
			<Item Name="Error Query.vi" Type="VI" URL="../../../../RageATE/Instruments/Agilent N5232A PNA-L/Labview Driver/Keysight PNA Series/Public/Utility/Error Query.vi"/>
			<Item Name="Reset.vi" Type="VI" URL="../../../../RageATE/Instruments/Agilent N5232A PNA-L/Labview Driver/Keysight PNA Series/Public/Utility/Reset.vi"/>
			<Item Name="Agilent MXA Series.lvlib" Type="Library" URL="../../../Instruments/Keysight N9010A/Agilent MXA Series/Agilent MXA Series.lvlib"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="WAM-PROD_Sequencer" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{E880CC06-C460-43E0-A823-099508FF353C}</Property>
				<Property Name="App_INI_GUID" Type="Str">{820DE559-AB06-4C11-A076-3D541176ADE2}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{A4DD66B5-7904-414B-A56B-56C780E89AB0}</Property>
				<Property Name="Bld_buildSpecDescription" Type="Str">INitial Release of WAM Test for Rage ATE</Property>
				<Property Name="Bld_buildSpecName" Type="Str">WAM-PROD_Sequencer</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">/C/WAM_Test_Application</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{88D728CE-BD6B-4845-BCD8-458D175A9EE7}</Property>
				<Property Name="Bld_version.build" Type="Int">3</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">WAM-TEST.exe</Property>
				<Property Name="Destination[0].path" Type="Path">/C/WAM_Test_Application/WAM-TEST.exe</Property>
				<Property Name="Destination[0].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">/C/WAM_Test_Application/SupportFiles</Property>
				<Property Name="Destination[1].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[2].destName" Type="Str">Support Directory 2</Property>
				<Property Name="Destination[2].path" Type="Path">/C/WAM_Test_Application/SupportFiles_2</Property>
				<Property Name="Destination[2].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[3].destName" Type="Str">Support Directory 3</Property>
				<Property Name="Destination[3].path" Type="Path">/C/WAM_Test_Application/SupportFiles_3</Property>
				<Property Name="Destination[3].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="DestinationCount" Type="Int">4</Property>
				<Property Name="Source[0].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[0].itemID" Type="Str">{010E3FF7-2423-48FA-B2BC-EE0F186C64E2}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[1].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[1].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">1</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/RageATE/Infrastructure</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[1].type" Type="Str">Container</Property>
				<Property Name="Source[10].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[10].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[10].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[10].itemID" Type="Ref">/My Computer/RageATE/Utilities</Property>
				<Property Name="Source[10].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[10].type" Type="Str">Container</Property>
				<Property Name="Source[11].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[11].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[11].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[11].destinationIndex" Type="Int">1</Property>
				<Property Name="Source[11].itemID" Type="Ref">/My Computer/Support/3500000_TetraProdSW</Property>
				<Property Name="Source[11].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[11].type" Type="Str">Container</Property>
				<Property Name="Source[12].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[12].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[12].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[12].destinationIndex" Type="Int">2</Property>
				<Property Name="Source[12].itemID" Type="Ref">/My Computer/Support/3500007_TetraFinalTestAnalysis</Property>
				<Property Name="Source[12].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[12].type" Type="Str">Container</Property>
				<Property Name="Source[13].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[13].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[13].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[13].destinationIndex" Type="Int">3</Property>
				<Property Name="Source[13].itemID" Type="Ref">/My Computer/Support/TetraLabGUI</Property>
				<Property Name="Source[13].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[13].type" Type="Str">Container</Property>
				<Property Name="Source[14].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[14].itemID" Type="Ref">/My Computer/WAM-PROD_Sequencer.vi</Property>
				<Property Name="Source[14].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[14].type" Type="Str">VI</Property>
				<Property Name="Source[15].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[15].itemID" Type="Ref">/My Computer/Support/imon_revc_limits.ini</Property>
				<Property Name="Source[15].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[16].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[16].itemID" Type="Ref">/My Computer/Support/imon_revLc_limits.ini</Property>
				<Property Name="Source[16].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[17].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[17].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[17].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[17].destinationIndex" Type="Int">3</Property>
				<Property Name="Source[17].itemID" Type="Ref">/My Computer/Support/FieldTestApp</Property>
				<Property Name="Source[17].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[17].type" Type="Str">Container</Property>
				<Property Name="Source[18].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[18].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[18].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[18].itemID" Type="Ref">/My Computer/RageATE/Zaber Gantry</Property>
				<Property Name="Source[18].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[18].type" Type="Str">Container</Property>
				<Property Name="Source[2].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[2].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[2].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">1</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/RageATE/Initialize References</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[2].type" Type="Str">Container</Property>
				<Property Name="Source[3].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[3].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">1</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/RageATE/Automated Tests/Tetra WAM/PRODUCTION/setup files</Property>
				<Property Name="Source[3].type" Type="Str">Container</Property>
				<Property Name="Source[4].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[4].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">1</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/RageATE</Property>
				<Property Name="Source[4].type" Type="Str">Container</Property>
				<Property Name="Source[5].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[5].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/RageATE/Automated Tests</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[5].type" Type="Str">Container</Property>
				<Property Name="Source[6].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[6].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[6].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[6].itemID" Type="Ref">/My Computer/RageATE/Calibration</Property>
				<Property Name="Source[6].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[6].type" Type="Str">Container</Property>
				<Property Name="Source[7].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[7].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[7].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[7].itemID" Type="Ref">/My Computer/RageATE/DLLs</Property>
				<Property Name="Source[7].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[7].type" Type="Str">Container</Property>
				<Property Name="Source[8].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[8].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[8].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[8].itemID" Type="Ref">/My Computer/RageATE/Labview Utilities</Property>
				<Property Name="Source[8].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[8].type" Type="Str">Container</Property>
				<Property Name="Source[9].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[9].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[9].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[9].itemID" Type="Ref">/My Computer/RageATE/Post Processors</Property>
				<Property Name="Source[9].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[9].type" Type="Str">Container</Property>
				<Property Name="SourceCount" Type="Int">19</Property>
				<Property Name="TgtF_companyName" Type="Str">RaGE Systems LLC</Property>
				<Property Name="TgtF_fileDescription" Type="Str">WAM-PROD_Sequencer</Property>
				<Property Name="TgtF_internalName" Type="Str">WAM-PROD_Sequencer</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2025 RaGE Systems LLC</Property>
				<Property Name="TgtF_productName" Type="Str">WAM-PROD_Sequencer</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{8CDC532E-FA09-4FC9-98C7-3342FB8E4CFE}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">WAM-TEST.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
