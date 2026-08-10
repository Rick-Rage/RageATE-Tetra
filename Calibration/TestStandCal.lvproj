<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="18008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="GetCalData.vi" Type="VI" URL="../GetCalData.vi"/>
		<Item Name="Read Sig Gen with PM.vi" Type="VI" URL="../Read Sig Gen with PM.vi"/>
		<Item Name="SetupSpectrumAnalyzerForCal.vi" Type="VI" URL="../SetupSpectrumAnalyzerForCal.vi"/>
		<Item Name="SpecAnMeasCW_Cal.vi" Type="VI" URL="../SpecAnMeasCW_Cal.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="compatReadText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatReadText.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="Open File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Open File+.vi"/>
				<Item Name="Read Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Read Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (I64).vi"/>
				<Item Name="Read Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (string).vi"/>
				<Item Name="Read Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet.vi"/>
				<Item Name="Read File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read File+ (string).vi"/>
				<Item Name="Read Lines From File (with error IO).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Lines From File (with error IO).vi"/>
				<Item Name="subTimeDelay.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/TimeDelayBlock.llb/subTimeDelay.vi"/>
			</Item>
			<Item Name="Agilent MXA Series.lvlib" Type="Library" URL="../../Instruments/Keysight N9010A/Agilent MXA Series/Agilent MXA Series.lvlib"/>
			<Item Name="FREQ_SPAN.vi" Type="VI" URL="../../Instruments/Keysight N9010A/FREQ_SPAN.vi"/>
			<Item Name="Instrument Mode.vi" Type="VI" URL="../../Instruments/Keysight N9010A/Instrument Mode.vi"/>
			<Item Name="REF_LEV.vi" Type="VI" URL="../../Instruments/Keysight N9010A/REF_LEV.vi"/>
			<Item Name="SA_ATT.vi" Type="VI" URL="../../Instruments/Keysight N9010A/SA_ATT.vi"/>
			<Item Name="SA_AVG.vi" Type="VI" URL="../../Instruments/Spectrum Analyzer/SA_AVG.vi"/>
			<Item Name="SA_GET_MARKER.vi" Type="VI" URL="../../Instruments/Spectrum Analyzer/SA_GET_MARKER.vi"/>
			<Item Name="SA_PREAMP.vi" Type="VI" URL="../../Instruments/Spectrum Analyzer/SA_PREAMP.vi"/>
			<Item Name="SA_RBW.vi" Type="VI" URL="../../Instruments/Keysight N9010A/SA_RBW.vi"/>
			<Item Name="SA_SET_CF.vi" Type="VI" URL="../../Instruments/Spectrum Analyzer/SA_SET_CF.vi"/>
			<Item Name="SA_SET_REFSRC.vi" Type="VI" URL="../../Instruments/Spectrum Analyzer/SA_SET_REFSRC.vi"/>
			<Item Name="Send Trigger and Wait for OPC.vi" Type="VI" URL="../../Instruments/Spectrum Analyzer/Send Trigger and Wait for OPC.vi"/>
			<Item Name="Station References Global.vi" Type="VI" URL="../../Initialize References/Station References Global.vi"/>
			<Item Name="SWEEP_CONT.vi" Type="VI" URL="../../Instruments/Keysight N9010A/SWEEP_CONT.vi"/>
			<Item Name="VISA_OPC.vi" Type="VI" URL="../../Instruments/VISA_OPC.vi"/>
			<Item Name="Visa_Reset_Clear.vi" Type="VI" URL="../../Instruments/VISA/Visa_Reset_Clear.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
