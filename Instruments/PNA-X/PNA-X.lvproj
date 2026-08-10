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
		<Item Name="Examples" Type="Folder">
			<Item Name="CompressionPT" Type="Folder">
				<Item Name="XaxisFreq.vi" Type="VI" URL="../Examples/CompressionPTExample/XaxisFreq.vi"/>
				<Item Name="CompPtGUI.vi" Type="VI" URL="../Examples/CompressionPTExample/CompPtGUI.vi"/>
				<Item Name="CompPtSetup.vi" Type="VI" URL="../Examples/CompressionPTExample/CompPtSetup.vi"/>
				<Item Name="CompressionPT.vi" Type="VI" URL="../Examples/CompressionPTExample/CompressionPT.vi"/>
			</Item>
			<Item Name="Harmonics" Type="Folder">
				<Item Name="Harmonics.vi" Type="VI" URL="../Examples/HarmonicsExample/Harmonics.vi"/>
			</Item>
			<Item Name="Intermods" Type="Folder">
				<Item Name="IMcalc.vi" Type="VI" URL="../Examples/IntermodsExample/IMcalc.vi"/>
				<Item Name="IMSetup.vi" Type="VI" URL="../Examples/IntermodsExample/IMSetup.vi"/>
				<Item Name="Intermods.vi" Type="VI" URL="../Examples/IntermodsExample/Intermods.vi"/>
			</Item>
			<Item Name="PowerCal" Type="Folder">
				<Item Name="PwrSwp.vi" Type="VI" URL="../Examples/PowerCalExample/PwrSwp.vi"/>
				<Item Name="PwrSwpExample.vi" Type="VI" URL="../Examples/PowerCalExample/PwrSwpExample.vi"/>
				<Item Name="PwrSwpGUI.vi" Type="VI" URL="../Examples/PowerCalExample/PwrSwpGUI.vi"/>
				<Item Name="RxPwr.vi" Type="VI" URL="../Examples/PowerCalExample/RxPwr.vi"/>
			</Item>
			<Item Name="SMC" Type="Folder">
				<Item Name="StrNumConv.vi" Type="VI" URL="../Examples/SmcExample/StrNumConv.vi"/>
				<Item Name="SMC.vi" Type="VI" URL="../Examples/SmcExample/SMC.vi"/>
				<Item Name="SMC_setup.vi" Type="VI" URL="../Examples/SmcExample/SMC_setup.vi"/>
				<Item Name="SMCGUI.vi" Type="VI" URL="../Examples/SmcExample/SMCGUI.vi"/>
				<Item Name="EX_SMC01.mxr" Type="Document" URL="/&lt;instrlib&gt;/PNA-X/Examples/SmcExample/EX_SMC01.mxr"/>
			</Item>
			<Item Name="SParameters" Type="Folder">
				<Item Name="UserInParse.vi" Type="VI" URL="../Examples/SParametersExample/UserInParse.vi"/>
				<Item Name="SParameters.vi" Type="VI" URL="../Examples/SParametersExample/SParameters.vi"/>
				<Item Name="SParmGUI.vi" Type="VI" URL="../Examples/SParametersExample/SParmGUI.vi"/>
				<Item Name="SParmSetup.vi" Type="VI" URL="../Examples/SParametersExample/SParmSetup.vi"/>
			</Item>
			<Item Name="TDR" Type="Folder">
				<Item Name="XaxisTime.vi" Type="VI" URL="../Examples/TdrExample/XaxisTime.vi"/>
				<Item Name="TDR.vi" Type="VI" URL="../Examples/TdrExample/TDR.vi"/>
				<Item Name="TDR_setup.vi" Type="VI" URL="../Examples/TdrExample/TDR_setup.vi"/>
			</Item>
			<Item Name="VMC" Type="Folder">
				<Item Name="VMC.vi" Type="VI" URL="../Examples/VmcExample/VMC.vi"/>
				<Item Name="VMC_setup.vi" Type="VI" URL="../Examples/VmcExample/VMC_setup.vi"/>
				<Item Name="VMCGUI.vi" Type="VI" URL="../Examples/VmcExample/VMCGUI.vi"/>
				<Item Name="EX_VMC01.mxr" Type="Document" URL="/&lt;instrlib&gt;/PNA-X/Examples/VmcExample/EX_VMC01.mxr"/>
			</Item>
			<Item Name="PNA-X.bin3" Type="Document" URL="/&lt;instrlib&gt;/PNA-X/Examples/PNA-X.bin3"/>
		</Item>
		<Item Name="RageATE-PNAX" Type="Folder">
			<Item Name="MMEM_DAT-FLAG.vi" Type="VI" URL="../RageATE-PNAX/MMEM_DAT-FLAG.vi"/>
			<Item Name="PNA-X_GetFileInfo.vi" Type="VI" URL="../RageATE-PNAX/PNA-X_GetFileInfo.vi"/>
		</Item>
		<Item Name="PNA-X.lvlib" Type="Library" URL="../PNA-X.lvlib"/>
		<Item Name="README.txt" Type="Document" URL="/&lt;instrlib&gt;/PNA-X/README.txt"/>
		<Item Name="dir.mnu" Type="Document" URL="/&lt;instrlib&gt;/PNA-X/dir.mnu"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="subTimeDelay.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/TimeDelayBlock.llb/subTimeDelay.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
			</Item>
			<Item Name="SYST_DATE-TIME.vi" Type="VI" URL="../Low Level/System/SYST_DATE-TIME.vi"/>
			<Item Name="PNA_Parse_Time-Date.vi" Type="VI" URL="../RageATE-PNAX/PNA_Parse_Time-Date.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
