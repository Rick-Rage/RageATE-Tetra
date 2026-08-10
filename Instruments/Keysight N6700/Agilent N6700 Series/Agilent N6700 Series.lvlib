<?xml version='1.0' encoding='UTF-8'?>
<Library LVVersion="18008000">
	<Property Name="Instrument Driver" Type="Str">True</Property>
	<Property Name="NI.Lib.Description" Type="Str">This driver configures and takes measurements from the Keysight/Agilent N6700 Series Power Supply. For more information about this driver, please refer to Agilent N6700 Series Readme.html</Property>
	<Property Name="NI.Lib.HelpPath" Type="Str"></Property>
	<Property Name="NI.Lib.Icon" Type="Bin">'!#!!!!!!!)!"1!&amp;!!!-!%!!!@````]!!!!"!!%!!!*%!!!*Q(C=\&gt;3R&lt;?.!%)8BZY-$QRE\-.4#Y$J1"1&lt;5QL3A6+&amp;3/ZP=&amp;YD!&amp;;"4#^/#7F!,^-`F7#*QA*3=!2`A8;^)P6XO@FL3F&amp;JZE/YVX#L\KW8M([&lt;D&gt;-&lt;RH&amp;X[TU0;&gt;-/Z@I26B]PY7@^Q_@&lt;XS@SYHSUW7`_[8V@,&gt;`^X```&gt;@[-Q:H.TU#=8[;Z*;5E,GN/M`&lt;IBS:-]S:-]S:-]S)-]S)-]S)0=S:X=S:X=S:X=S)X=S)X=S)W]68+2CVTE\%KS?,*1-GES14)9CJ+0R*.Y%E`CY;M34_**0)EH]4"%C3@R**\%EXCY4)EH]33?R*.YG+J*MF6S0)G([26Y!E`A#4S"BS56?!*!M&amp;AQ=4!*$!7&gt;Q5HA#4S"BV-&amp;HM!4?!*0Y+&amp;&lt;A3@Q"*\!%XCYJ/V+.-V9S@%QD2S0YX%]DM@R-,5=D_.R0)\(]&lt;#=()`D=2$/AM\E%/2=Z!RQPDA?R]."DM@R/"\(YXDI;H@)W][-GL'3YT%]BM@Q'"\$QR1S0)&lt;(]"A?Q]/U-DS'R`!9(M0$5D)]BM@Q'""D5:;8-:FRI4()#!Q0@_VJM8;8IEGMV@L8H"Z5V1/I?L"5$YTK16$&gt;9.7.5^U1V5;L.F#V-;I@L0IB+K"K9&gt;7%KI%[]8GE(7A^&lt;5N&lt;UV;U*7V"[]:,``(!U_GEY`'IQ_'APO_VX7[V8K_V7KWU8#[V7#T5&gt;&gt;XZ&lt;@6%H=L&gt;RXNJQ`H,W\Z\`@GY[X_`\P\]?N\NXF[[-@`-.LW8PM+\54]UT&amp;\T\.%\,[7H&lt;!!!!!!</Property>
	<Property Name="NI.Lib.SourceVersion" Type="Int">402685952</Property>
	<Property Name="NI.Lib.Version" Type="Str">3.2.0.0</Property>
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">false</Property>
	<Property Name="NI.SortType" Type="Int">3</Property>
	<Item Name="Public" Type="Folder">
		<Property Name="NI.LibItem.Scope" Type="Int">1</Property>
		<Item Name="Action-Status" Type="Folder">
			<Item Name="Abort Acquisition.vi" Type="VI" URL="../Public/Action-Status/Abort Acquisition.vi"/>
			<Item Name="Abort Output Trigger.vi" Type="VI" URL="../Public/Action-Status/Abort Output Trigger.vi"/>
			<Item Name="Channel Grouping Status.vi" Type="VI" URL="../Public/Action-Status/Channel Grouping Status.vi"/>
			<Item Name="Immediate Acquisition Trigger.vi" Type="VI" URL="../Public/Action-Status/Immediate Acquisition Trigger.vi"/>
			<Item Name="Immediate Data Log Trigger.vi" Type="VI" URL="../Public/Action-Status/Immediate Data Log Trigger.vi"/>
			<Item Name="Immediate External Data Log Trigger.vi" Type="VI" URL="../Public/Action-Status/Immediate External Data Log Trigger.vi"/>
			<Item Name="Immediate Histogram Trigger.vi" Type="VI" URL="../Public/Action-Status/Immediate Histogram Trigger.vi"/>
			<Item Name="Immediate Transient Trigger.vi" Type="VI" URL="../Public/Action-Status/Immediate Transient Trigger.vi"/>
			<Item Name="Initiate Acquisition.vi" Type="VI" URL="../Public/Action-Status/Initiate Acquisition.vi"/>
			<Item Name="Initiate Output Trigger.vi" Type="VI" URL="../Public/Action-Status/Initiate Output Trigger.vi"/>
			<Item Name="Query Histogram.vi" Type="VI" URL="../Public/Action-Status/Query Histogram.vi"/>
			<Item Name="Query Max Current Limit.vi" Type="VI" URL="../Public/Action-Status/Query Max Current Limit.vi"/>
			<Item Name="Query Max Voltage Level.vi" Type="VI" URL="../Public/Action-Status/Query Max Voltage Level.vi"/>
			<Item Name="Query Output State.vi" Type="VI" URL="../Public/Action-Status/Query Output State.vi"/>
			<Item Name="Query Quality of Waveform.vi" Type="VI" URL="../Public/Action-Status/Query Quality of Waveform.vi"/>
			<Item Name="Reset Output Protection.vi" Type="VI" URL="../Public/Action-Status/Reset Output Protection.vi"/>
			<Item Name="Send Software Trigger.vi" Type="VI" URL="../Public/Action-Status/Send Software Trigger.vi"/>
			<Item Name="Ungroup Channels.vi" Type="VI" URL="../Public/Action-Status/Ungroup Channels.vi"/>
		</Item>
		<Item Name="Configuration" Type="Folder">
			<Item Name="Data Log" Type="Folder">
				<Item Name="Configure Data Log Markers.vi" Type="VI" URL="../Public/Configuration/Data Log/Configure Data Log Markers.vi"/>
				<Item Name="Configure Data Log Measurement Range.vi" Type="VI" URL="../Public/Configuration/Data Log/Configure Data Log Measurement Range.vi"/>
				<Item Name="Configure Data Log.vi" Type="VI" URL="../Public/Configuration/Data Log/Configure Data Log.vi"/>
			</Item>
			<Item Name="Digital" Type="Folder">
				<Item Name="Configure Pin.vi" Type="VI" URL="../Public/Configuration/Digital/Configure Pin.vi"/>
				<Item Name="Read Input Port.vi" Type="VI" URL="../Public/Configuration/Digital/Read Input Port.vi"/>
				<Item Name="Write To Output Port.vi" Type="VI" URL="../Public/Configuration/Digital/Write To Output Port.vi"/>
			</Item>
			<Item Name="Exeternal Data Log" Type="Folder">
				<Item Name="Auto External Data Log Range.vi" Type="VI" URL="../Public/Configuration/External Data Log/Auto External Data Log Range.vi"/>
				<Item Name="Configure External Data Log Range.vi" Type="VI" URL="../Public/Configuration/External Data Log/Configure External Data Log Range.vi"/>
				<Item Name="Configure External Data Log.vi" Type="VI" URL="../Public/Configuration/External Data Log/Configure External Data Log.vi"/>
			</Item>
			<Item Name="Group" Type="Folder">
				<Item Name="Configure Channel Grouping.vi" Type="VI" URL="../Public/Configuration/Group/Configure Channel Grouping.vi"/>
			</Item>
			<Item Name="Histogram" Type="Folder">
				<Item Name="Configure Histogram.vi" Type="VI" URL="../Public/Configuration/Histogram/Configure Histogram.vi"/>
			</Item>
			<Item Name="Measurement" Type="Folder">
				<Item Name="Configure Measurement Range.vi" Type="VI" URL="../Public/Configuration/Measurement/Configure Measurement Range.vi"/>
				<Item Name="Configure Measurement Resolution.vi" Type="VI" URL="../Public/Configuration/Measurement/Configure Measurement Resolution.vi"/>
				<Item Name="Configure Measurement Window.vi" Type="VI" URL="../Public/Configuration/Measurement/Configure Measurement Window.vi"/>
				<Item Name="Configure Measurement.vi" Type="VI" URL="../Public/Configuration/Measurement/Configure Measurement.vi"/>
				<Item Name="Configure Simultaneous Measurement.vi" Type="VI" URL="../Public/Configuration/Measurement/Configure Simultaneous Measurement.vi"/>
			</Item>
			<Item Name="Output" Type="Folder">
				<Item Name="Configure ASP Over Voltage Protection Delay.vi" Type="VI" URL="../Public/Configuration/Output/Configure ASP Over Voltage Protection Delay.vi"/>
				<Item Name="Configure Current Limit.vi" Type="VI" URL="../Public/Configuration/Output/Configure Current Limit.vi"/>
				<Item Name="Configure Output Delay.vi" Type="VI" URL="../Public/Configuration/Output/Configure Output Delay.vi"/>
				<Item Name="Configure Output Enabled.vi" Type="VI" URL="../Public/Configuration/Output/Configure Output Enabled.vi"/>
				<Item Name="Configure Output Protection.vi" Type="VI" URL="../Public/Configuration/Output/Configure Output Protection.vi"/>
				<Item Name="Configure Output Range.vi" Type="VI" URL="../Public/Configuration/Output/Configure Output Range.vi"/>
				<Item Name="Configure Output Regulation.vi" Type="VI" URL="../Public/Configuration/Output/Configure Output Regulation.vi"/>
				<Item Name="Configure Over Voltage Protection.vi" Type="VI" URL="../Public/Configuration/Output/Configure Over Voltage Protection.vi"/>
				<Item Name="Configure Relay Polarity.vi" Type="VI" URL="../Public/Configuration/Output/Configure Relay Polarity.vi"/>
				<Item Name="Configure SMU Bandwidth Oscillation.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Bandwidth Oscillation.vi"/>
				<Item Name="Configure SMU Current Limit Tracking.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Current Limit Tracking.vi"/>
				<Item Name="Configure SMU Current Slew Rate.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Current Slew Rate.vi"/>
				<Item Name="Configure SMU Negative Current Limit.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Negative Current Limit.vi"/>
				<Item Name="Configure SMU Negative Over Voltage Remote Protection.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Negative Over Voltage Remote Protection.vi"/>
				<Item Name="Configure SMU Negative Voltage Limit.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Negative Voltage Limit.vi"/>
				<Item Name="Configure SMU Output Impedance.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Output Impedance.vi"/>
				<Item Name="Configure SMU Output Resistance.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Output Resistance.vi"/>
				<Item Name="Configure SMU Positive Current Limit.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Positive Current Limit.vi"/>
				<Item Name="Configure SMU Positive Over Voltage Remote Protection.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Positive Over Voltage Remote Protection.vi"/>
				<Item Name="Configure SMU Positive Voltage Limit.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Positive Voltage Limit.vi"/>
				<Item Name="Configure SMU Voltage Limit Tracking.vi" Type="VI" URL="../Public/Configuration/Output/Configure SMU Voltage Limit Tracking.vi"/>
				<Item Name="Configure Voltage Level.vi" Type="VI" URL="../Public/Configuration/Output/Configure Voltage Level.vi"/>
				<Item Name="Limit Channel Power.vi" Type="VI" URL="../Public/Configuration/Output/Limit Channel Power.vi"/>
			</Item>
			<Item Name="Triggering" Type="Folder">
				<Item Name="Data Log" Type="Folder">
					<Item Name="Configure Data Log Trigger Source.vi" Type="VI" URL="../Public/Configuration/Triggering/Data Log/Configure Data Log Trigger Source.vi"/>
					<Item Name="Configure Data Log Trigger.vi" Type="VI" URL="../Public/Configuration/Triggering/Data Log/Configure Data Log Trigger.vi"/>
				</Item>
				<Item Name="List" Type="Folder">
					<Item Name="Configure Current List.vi" Type="VI" URL="../Public/Configuration/Triggering/List/Configure Current List.vi"/>
					<Item Name="Configure Dwell List.vi" Type="VI" URL="../Public/Configuration/Triggering/List/Configure Dwell List.vi"/>
					<Item Name="Configure List.vi" Type="VI" URL="../Public/Configuration/Triggering/List/Configure List.vi"/>
					<Item Name="Configure Voltage List.vi" Type="VI" URL="../Public/Configuration/Triggering/List/Configure Voltage List.vi"/>
				</Item>
				<Item Name="Trigger Output" Type="Folder">
					<Item Name="Configure BOST List.vi" Type="VI" URL="../Public/Configuration/Triggering/Trigger Output/Configure BOST List.vi"/>
					<Item Name="Configure EOST List.vi" Type="VI" URL="../Public/Configuration/Triggering/Trigger Output/Configure EOST List.vi"/>
				</Item>
				<Item Name="Configure External Data Log Trigger Source.vi" Type="VI" URL="../Public/Configuration/Triggering/Configure External Data Log Trigger Source.vi"/>
				<Item Name="Configure Histogram Trigger Source.vi" Type="VI" URL="../Public/Configuration/Triggering/Configure Histogram Trigger Source.vi"/>
				<Item Name="Configure Trigger Source.vi" Type="VI" URL="../Public/Configuration/Triggering/Configure Trigger Source.vi"/>
				<Item Name="Configure Triggered Current Limit.vi" Type="VI" URL="../Public/Configuration/Triggering/Configure Triggered Current Limit.vi"/>
				<Item Name="Configure Triggered Current Mode.vi" Type="VI" URL="../Public/Configuration/Triggering/Configure Triggered Current Mode.vi"/>
				<Item Name="Configure Triggered Voltage Level.vi" Type="VI" URL="../Public/Configuration/Triggering/Configure Triggered Voltage Level.vi"/>
				<Item Name="Configure Triggered Voltage Mode.vi" Type="VI" URL="../Public/Configuration/Triggering/Configure Triggered Voltage Mode.vi"/>
				<Item Name="Configure Waveform Trigger Source.vi" Type="VI" URL="../Public/Configuration/Triggering/Configure Waveform Trigger Source.vi"/>
			</Item>
			<Item Name="Waveform" Type="Folder">
				<Item Name="Sequence" Type="Folder">
					<Item Name="Configure Sequence.vi" Type="VI" URL="../Public/Configuration/Waveform/Sequence/Configure Sequence.vi"/>
					<Item Name="Configure Sequence (Exponential).vi" Type="VI" URL="../Public/Configuration/Waveform/Sequence/Configure Sequence (Exponential).vi"/>
					<Item Name="Configure Sequence (Pulse).vi" Type="VI" URL="../Public/Configuration/Waveform/Sequence/Configure Sequence (Pulse).vi"/>
					<Item Name="Configure Sequence (Ramp).vi" Type="VI" URL="../Public/Configuration/Waveform/Sequence/Configure Sequence (Ramp).vi"/>
					<Item Name="Configure Sequence (Sine Wave).vi" Type="VI" URL="../Public/Configuration/Waveform/Sequence/Configure Sequence (Sine Wave).vi"/>
					<Item Name="Configure Sequence (Staircase).vi" Type="VI" URL="../Public/Configuration/Waveform/Sequence/Configure Sequence (Staircase).vi"/>
					<Item Name="Configure Sequence (Step).vi" Type="VI" URL="../Public/Configuration/Waveform/Sequence/Configure Sequence (Step).vi"/>
					<Item Name="Configure Sequence (Trapezoid).vi" Type="VI" URL="../Public/Configuration/Waveform/Sequence/Configure Sequence (Trapezoid).vi"/>
					<Item Name="Configure Sequence (User Defined).vi" Type="VI" URL="../Public/Configuration/Waveform/Sequence/Configure Sequence (User Defined).vi"/>
					<Item Name="Configure Sequence Characteristics.vi" Type="VI" URL="../Public/Configuration/Waveform/Sequence/Configure Sequence Characteristics.vi"/>
				</Item>
				<Item Name="Configure Waveform.vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform.vi"/>
				<Item Name="Configure Waveform (Constant Dwell).vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform (Constant Dwell).vi"/>
				<Item Name="Configure Waveform (Exponential).vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform (Exponential).vi"/>
				<Item Name="Configure Waveform (Pulse).vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform (Pulse).vi"/>
				<Item Name="Configure Waveform (Ramp).vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform (Ramp).vi"/>
				<Item Name="Configure Waveform (Sine Wave).vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform (Sine Wave).vi"/>
				<Item Name="Configure Waveform (Staircase).vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform (Staircase).vi"/>
				<Item Name="Configure Waveform (Step).vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform (Step).vi"/>
				<Item Name="Configure Waveform (Trapezoid).vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform (Trapezoid).vi"/>
				<Item Name="Configure Waveform (User Defined).vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform (User Defined).vi"/>
				<Item Name="Configure Waveform Characteristics.vi" Type="VI" URL="../Public/Configuration/Waveform/Configure Waveform Characteristics.vi"/>
			</Item>
		</Item>
		<Item Name="Data" Type="Folder">
			<Item Name="Low Level" Type="Folder">
				<Item Name="Abort Data Log.vi" Type="VI" URL="../Public/Data/Low Level/Abort Data Log.vi"/>
				<Item Name="Abort External Data Log.vi" Type="VI" URL="../Public/Data/Low Level/Abort External Data Log.vi"/>
				<Item Name="Abort Histogram.vi" Type="VI" URL="../Public/Data/Low Level/Abort Histogram.vi"/>
				<Item Name="Fetch Data Log.vi" Type="VI" URL="../Public/Data/Low Level/Fetch Data Log.vi"/>
				<Item Name="Fetch External Data Log.vi" Type="VI" URL="../Public/Data/Low Level/Fetch External Data Log.vi"/>
				<Item Name="Fetch Histogram.vi" Type="VI" URL="../Public/Data/Low Level/Fetch Histogram.vi"/>
				<Item Name="Initiate Data Log.vi" Type="VI" URL="../Public/Data/Low Level/Initiate Data Log.vi"/>
				<Item Name="Initiate External Data Log.vi" Type="VI" URL="../Public/Data/Low Level/Initiate External Data Log.vi"/>
				<Item Name="Initiate Histogram.vi" Type="VI" URL="../Public/Data/Low Level/Initiate Histogram.vi"/>
			</Item>
			<Item Name="Read Histogram.vi" Type="VI" URL="../Public/Data/Read Histogram.vi"/>
		</Item>
		<Item Name="Measure Output" Type="Folder">
			<Item Name="Fetch Array.vi" Type="VI" URL="../Public/Measure Output/Fetch Array.vi"/>
			<Item Name="Fetch.vi" Type="VI" URL="../Public/Measure Output/Fetch.vi"/>
			<Item Name="Measure Array.vi" Type="VI" URL="../Public/Measure Output/Measure Array.vi"/>
			<Item Name="Measure.vi" Type="VI" URL="../Public/Measure Output/Measure.vi"/>
		</Item>
		<Item Name="Utility" Type="Folder">
			<Item Name="Error Message.vi" Type="VI" URL="../Public/Utility/Error Message.vi"/>
			<Item Name="Error Query (Multiple).vi" Type="VI" URL="../Public/Utility/Error Query (Multiple).vi"/>
			<Item Name="Error Query.vi" Type="VI" URL="../Public/Utility/Error Query.vi"/>
			<Item Name="Reset.vi" Type="VI" URL="../Public/Utility/Reset.vi"/>
			<Item Name="Revision Query.vi" Type="VI" URL="../Public/Utility/Revision Query.vi"/>
			<Item Name="Self-Test.vi" Type="VI" URL="../Public/Utility/Self-Test.vi"/>
			<Item Name="Convert Waveform To User Defined List.vi" Type="VI" URL="../Public/Utility/Convert Waveform To User Defined List.vi"/>
			<Item Name="Change Instrument Identity.vi" Type="VI" URL="../Public/Utility/Change Instrument Identity.vi"/>
			<Item Name="File Management.vi" Type="VI" URL="../Public/Utility/File Management.vi"/>
			<Item Name="Get Channel Model Number.vi" Type="VI" URL="../Public/Utility/Get Channel Model Number.vi"/>
			<Item Name="Reset Sequence.vi" Type="VI" URL="../Public/Utility/Reset Sequence.vi"/>
			<Item Name="Save Recall Sequence.vi" Type="VI" URL="../Public/Utility/Save Recall Sequence.vi"/>
		</Item>
		<Item Name="Obsolete" Type="Folder">
			<Item Name="Abort.vi" Type="VI" URL="../Public/Obsolete/Abort.vi"/>
			<Item Name="Configure OVP.vi" Type="VI" URL="../Public/Obsolete/Configure OVP.vi"/>
			<Item Name="Initiate.vi" Type="VI" URL="../Public/Obsolete/Initiate.vi"/>
		</Item>
		<Item Name="Close.vi" Type="VI" URL="../Public/Close.vi"/>
		<Item Name="Initialize.vi" Type="VI" URL="../Public/Initialize.vi"/>
	</Item>
	<Item Name="Private" Type="Folder">
		<Property Name="NI.LibItem.Scope" Type="Int">2</Property>
		<Item Name="Default Instrument Setup.vi" Type="VI" URL="../Private/Default Instrument Setup.vi"/>
	</Item>
</Library>
