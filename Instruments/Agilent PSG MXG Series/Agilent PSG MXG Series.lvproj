<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="18008000">
	<Property Name="Instrument Driver" Type="Str">True</Property>
	<Property Name="NI.Project.Description" Type="Str">This project is used by developers to edit API and example files for LabVIEW Plug and Play instrument drivers.</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="CCSymbols" Type="Str">OS,Win;CPU,x86;</Property>
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Agilent PSG MXG Series" Type="Folder">
			<Item Name="Examples" Type="Folder">
				<Item Name="Agilent PSG MXG Series Analog Modulation.vi" Type="VI" URL="../Examples/Agilent PSG MXG Series Analog Modulation.vi"/>
				<Item Name="Agilent PSG MXG Series BERT Using Custom Digital Modulation.vi" Type="VI" URL="../Examples/Agilent PSG MXG Series BERT Using Custom Digital Modulation.vi"/>
				<Item Name="Agilent PSG MXG Series Configure Frequency Power.vi" Type="VI" URL="../Examples/Agilent PSG MXG Series Configure Frequency Power.vi"/>
				<Item Name="Agilent PSG MXG Series Configure Low Frequency Output.vi" Type="VI" URL="../Examples/Agilent PSG MXG Series Configure Low Frequency Output.vi"/>
				<Item Name="Agilent PSG MXG Series Digital Modulation.vi" Type="VI" URL="../Examples/Agilent PSG MXG Series Digital Modulation.vi"/>
				<Item Name="Agilent PSG MXG Series List Sweep.vi" Type="VI" URL="../Examples/Agilent PSG MXG Series List Sweep.vi"/>
				<Item Name="Agilent PSG MXG Series Operate N5102A Module in Output Mode.vi" Type="VI" URL="../Examples/Agilent PSG MXG Series Operate N5102A Module in Output Mode.vi"/>
				<Item Name="Agilent PSG MXG Series.bin3" Type="Document" URL="../Examples/Agilent PSG MXG Series.bin3"/>
				<Item Name="UserFlatness - Copy.vi" Type="VI" URL="../Examples/UserFlatness - Copy.vi"/>
				<Item Name="UserFlatness3.vi" Type="VI" URL="../Examples/UserFlatness3.vi"/>
			</Item>
			<Item Name="express" Type="Folder">
				<Item Name="Utility" Type="Folder">
					<Item Name="Resource" Type="Folder">
						<Item Name="icon.png" Type="Document" URL="../express/Utility/Resource/icon.png"/>
					</Item>
					<Item Name="StudioHelper" Type="Folder">
						<Item Name="CommandParser" Type="Folder">
							<Item Name="Interface" Type="Folder">
								<Item Name="parse_cmd.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Interface/parse_cmd.vi"/>
							</Item>
							<Item Name="Methods" Type="Folder">
								<Item Name="ExtractParameters" Type="Folder">
									<Item Name="Interface" Type="Folder">
										<Item Name="extract_para_from_command.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/ExtractParameters/Interface/extract_para_from_command.vi"/>
									</Item>
									<Item Name="Methods" Type="Folder">
										<Item Name="is_boolean_control.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/ExtractParameters/Methods/is_boolean_control.vi"/>
										<Item Name="is_numeric_control.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/ExtractParameters/Methods/is_numeric_control.vi"/>
									</Item>
								</Item>
								<Item Name="PolishInstrumentCommand" Type="Folder">
									<Item Name="Interface" Type="Folder">
										<Item Name="polish_instrument_command.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Interface/polish_instrument_command.vi"/>
									</Item>
									<Item Name="Methods" Type="Folder">
										<Item Name="PostModification" Type="Folder">
											<Item Name="Interface" Type="Folder">
												<Item Name="post_modification.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PostModification/Interface/post_modification.vi"/>
											</Item>
											<Item Name="Internal" Type="Folder">
												<Item Name="remove_outside_pairs_on_inside_pairs.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PostModification/Internal/remove_outside_pairs_on_inside_pairs.vi"/>
											</Item>
											<Item Name="Methods" Type="Folder">
												<Item Name="add_open_brace.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PostModification/Methods/add_open_brace.vi"/>
												<Item Name="remove_content_in_[].vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PostModification/Methods/remove_content_in_[].vi"/>
												<Item Name="remove_lower_case.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PostModification/Methods/remove_lower_case.vi"/>
												<Item Name="remove_redundant_open_brace.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PostModification/Methods/remove_redundant_open_brace.vi"/>
												<Item Name="remove_special_characters.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PostModification/Methods/remove_special_characters.vi"/>
											</Item>
										</Item>
										<Item Name="PreModification" Type="Folder">
											<Item Name="Interface" Type="Folder">
												<Item Name="pre_modification.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PreModification/Interface/pre_modification.vi"/>
											</Item>
											<Item Name="Methods" Type="Folder">
												<Item Name="remove_extra_space_character.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PreModification/Methods/remove_extra_space_character.vi"/>
												<Item Name="remove_start_end_space.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PreModification/Methods/remove_start_end_space.vi"/>
												<Item Name="replace_boolean_with_on_off.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PreModification/Methods/replace_boolean_with_on_off.vi"/>
												<Item Name="replace_cmds_option.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/PreModification/Methods/replace_cmds_option.vi"/>
											</Item>
										</Item>
										<Item Name="SpecialModification" Type="Folder">
											<Item Name="Interface" Type="Folder">
												<Item Name="special_modification.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Interface/special_modification.vi"/>
											</Item>
											<Item Name="Internals" Type="Folder">
												<Item Name="find_repeat_parameters_1.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Internals/find_repeat_parameters_1.vi"/>
												<Item Name="find_repeat_parameters_2.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Internals/find_repeat_parameters_2.vi"/>
												<Item Name="find_repeat_parameters_3.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Internals/find_repeat_parameters_3.vi"/>
												<Item Name="find_special_character.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Internals/find_special_character.vi"/>
												<Item Name="has_repeated_capability_solution.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Internals/has_repeated_capability_solution.vi"/>
											</Item>
											<Item Name="Methods" Type="Folder">
												<Item Name="brace_space_inside_brace.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Methods/brace_space_inside_brace.vi"/>
												<Item Name="brace_space_inside_brace_solution.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Methods/brace_space_inside_brace_solution.vi"/>
												<Item Name="has_[n].vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Methods/has_[n].vi"/>
												<Item Name="has_[n]_solution.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Methods/has_[n]_solution.vi"/>
												<Item Name="repeated_capability_parameters.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Methods/repeated_capability_parameters.vi"/>
												<Item Name="square_brackets_beside_vertical_bar.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Methods/square_brackets_beside_vertical_bar.vi"/>
												<Item Name="vertical_bar_inside_brackets.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Methods/vertical_bar_inside_brackets.vi"/>
												<Item Name="vertical_bar_inside_brackets_solution.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Methods/PolishInstrumentCommand/Methods/SpecialModification/Methods/vertical_bar_inside_brackets_solution.vi"/>
											</Item>
										</Item>
									</Item>
								</Item>
							</Item>
							<Item Name="Micellaneous" Type="Folder">
								<Item Name="find_special_character_pairs.vi" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/Micellaneous/find_special_character_pairs.vi"/>
							</Item>
							<Item Name="TypeDefinitions" Type="Folder">
								<Item Name="auto_extracted_control_spec.ctl" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/TypeDefinitions/auto_extracted_control_spec.ctl"/>
								<Item Name="auto_extracted_control_specs.ctl" Type="VI" URL="../express/Utility/StudioHelper/CommandParser/TypeDefinitions/auto_extracted_control_specs.ctl"/>
							</Item>
						</Item>
						<Item Name="Common" Type="Folder">
							<Item Name="VI Scripting" Type="Folder">
								<Item Name="Type Define" Type="Folder"/>
								<Item Name="VI" Type="Folder">
									<Item Name="Connector" Type="Folder">
										<Item Name="Method" Type="Folder"/>
									</Item>
									<Item Name="Diagram" Type="Folder">
										<Item Name="Method" Type="Folder"/>
										<Item Name="Terminal" Type="Folder">
											<Item Name="Method" Type="Folder"/>
										</Item>
									</Item>
									<Item Name="Execution" Type="Folder"/>
									<Item Name="Front Panel" Type="Folder">
										<Item Name="Attribute" Type="Folder"/>
										<Item Name="Method" Type="Folder">
											<Item Name="Clear" Type="Folder"/>
										</Item>
									</Item>
									<Item Name="Object" Type="Folder">
										<Item Name="Method" Type="Folder"/>
									</Item>
								</Item>
								<Item Name="NISAST VI Scripting.lvlib" Type="Library" URL="../../Keysight N9010A/Agilent MXA Series/express/Utility/StudioHelper/Common/VI Scripting/NISAST VI Scripting.lvlib"/>
							</Item>
						</Item>
						<Item Name="Gtor" Type="Folder">
							<Item Name="Mth" Type="Folder">
								<Item Name="GenVI" Type="Folder">
									<Item Name="Intf" Type="Folder">
										<Item Name="GenStdVI" Type="Folder">
											<Item Name="Mth" Type="Folder">
												<Item Name="GenOneStdVI" Type="Folder">
													<Item Name="Intf" Type="Folder">
														<Item Name="generate_single_vi.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Intf/generate_single_vi.vi"/>
													</Item>
													<Item Name="Iternl" Type="Folder">
														<Item Name="AddObj" Type="Folder">
															<Item Name="AddControl" Type="Folder">
																<Item Name="Interface" Type="Folder">
																	<Item Name="add_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Interface/add_control.vi"/>
																</Item>
																<Item Name="Internal" Type="Folder">
																	<Item Name="add_customize_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Internal/add_customize_control.vi"/>
																	<Item Name="add_specific_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Internal/add_specific_control.vi"/>
																</Item>
																<Item Name="Methods" Type="Folder">
																	<Item Name="add_array_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Methods/add_array_control.vi"/>
																	<Item Name="add_boolean_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Methods/add_boolean_control.vi"/>
																	<Item Name="add_error_in_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Methods/add_error_in_control.vi"/>
																	<Item Name="add_error_out_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Methods/add_error_out_control.vi"/>
																	<Item Name="add_numeric_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Methods/add_numeric_control.vi"/>
																	<Item Name="add_ring_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Methods/add_ring_control.vi"/>
																	<Item Name="add_string_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Methods/add_string_control.vi"/>
																	<Item Name="add_visa_in_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Methods/add_visa_in_control.vi"/>
																	<Item Name="add_visa_out_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Methods/add_visa_out_control.vi"/>
																	<Item Name="add_waveform_control.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/Methods/add_waveform_control.vi"/>
																</Item>
																<Item Name="TypeDefinitions" Type="Folder">
																	<Item Name="bd_control_type.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/AddControl/TypeDefinitions/bd_control_type.ctl"/>
																</Item>
															</Item>
															<Item Name="Miscellaneous" Type="Folder">
																<Item Name="get_specified_representation.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/AddObj/Miscellaneous/get_specified_representation.vi"/>
															</Item>
														</Item>
														<Item Name="CalPos" Type="Folder">
															<Item Name="CmdToStr" Type="Folder">
																<Item Name="Intf" Type="Folder">
																	<Item Name="cal_cmd_to_string_position.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/CmdToStr/Intf/cal_cmd_to_string_position.vi"/>
																</Item>
																<Item Name="Mth" Type="Folder">
																	<Item Name="cal_1st_sub_node_x_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/CmdToStr/Mth/cal_1st_sub_node_x_pos.vi"/>
																	<Item Name="cal_main_bool_const_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/CmdToStr/Mth/cal_main_bool_const_pos.vi"/>
																	<Item Name="cal_main_format_const_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/CmdToStr/Mth/cal_main_format_const_pos.vi"/>
																	<Item Name="cal_main_format_node_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/CmdToStr/Mth/cal_main_format_node_pos.vi"/>
																	<Item Name="cal_main_node_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/CmdToStr/Mth/cal_main_node_pos.vi"/>
																</Item>
																<Item Name="TypeDefinitions" Type="Folder">
																	<Item Name="main_position_types.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/CmdToStr/TypeDefinitions/main_position_types.ctl"/>
																</Item>
															</Item>
															<Item Name="InstIntf" Type="Folder">
																<Item Name="Methods" Type="Folder">
																	<Item Name="cal_error_out_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/InstIntf/Methods/cal_error_out_pos.vi"/>
																	<Item Name="cal_visa_in_error_in_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/InstIntf/Methods/cal_visa_in_error_in_pos.vi"/>
																	<Item Name="cal_visa_out_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/InstIntf/Methods/cal_visa_out_pos.vi"/>
																</Item>
															</Item>
															<Item Name="ParaToStr" Type="Folder">
																<Item Name="Intf" Type="Folder">
																	<Item Name="cal_para_to_string_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/ParaToStr/Intf/cal_para_to_string_pos.vi"/>
																</Item>
																<Item Name="Mth" Type="Folder">
																	<Item Name="cal_sub_bool_const_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/ParaToStr/Mth/cal_sub_bool_const_pos.vi"/>
																	<Item Name="cal_sub_bool_node_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/ParaToStr/Mth/cal_sub_bool_node_pos.vi"/>
																	<Item Name="cal_sub_numeric_string_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/ParaToStr/Mth/cal_sub_numeric_string_pos.vi"/>
																	<Item Name="cal_sub_ring_const_pos.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/ParaToStr/Mth/cal_sub_ring_const_pos.vi"/>
																</Item>
																<Item Name="TypeDefinitions" Type="Folder">
																	<Item Name="sub_position_type.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/CalPos/ParaToStr/TypeDefinitions/sub_position_type.ctl"/>
																</Item>
															</Item>
														</Item>
														<Item Name="ConttWire" Type="Folder">
															<Item Name="Internal" Type="Folder">
																<Item Name="get_term_index.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/ConttWire/Internal/get_term_index.vi"/>
															</Item>
															<Item Name="Methods" Type="Folder">
																<Item Name="connect_two_terminal.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/ConttWire/Methods/connect_two_terminal.vi"/>
																<Item Name="connect_with_last_node_term.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/ConttWire/Methods/connect_with_last_node_term.vi"/>
															</Item>
															<Item Name="TypeDefines" Type="Folder">
																<Item Name="connect_with_last_node_types.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/ConttWire/TypeDefines/connect_with_last_node_types.ctl"/>
															</Item>
														</Item>
														<Item Name="ConverttStr" Type="Folder">
															<Item Name="Interface" Type="Folder">
																<Item Name="convert_strings.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/ConverttStr/Interface/convert_strings.vi"/>
															</Item>
															<Item Name="Methods" Type="Folder">
																<Item Name="convert_boolean_command.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/ConverttStr/Methods/convert_boolean_command.vi"/>
																<Item Name="convert_ring_command.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/ConverttStr/Methods/convert_ring_command.vi"/>
															</Item>
															<Item Name="TypeDefinitions" Type="Folder">
																<Item Name="conver_strings_types.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/ConverttStr/TypeDefinitions/conver_strings_types.ctl"/>
															</Item>
														</Item>
														<Item Name="GetNodeTerm" Type="Folder">
															<Item Name="Methods" Type="Folder">
																<Item Name="get_visa_write_node_term.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/GetNodeTerm/Methods/get_visa_write_node_term.vi"/>
															</Item>
															<Item Name="StringProcessingNode" Type="Folder">
																<Item Name="Interface" Type="Folder">
																	<Item Name="get_string_node_terms.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/GetNodeTerm/StringProcessingNode/Interface/get_string_node_terms.vi"/>
																</Item>
																<Item Name="Methods" Type="Folder">
																	<Item Name="get_bool_node_term.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/GetNodeTerm/StringProcessingNode/Methods/get_bool_node_term.vi"/>
																	<Item Name="get_concatenate_node_term.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/GetNodeTerm/StringProcessingNode/Methods/get_concatenate_node_term.vi"/>
																	<Item Name="get_format_node_term.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/GetNodeTerm/StringProcessingNode/Methods/get_format_node_term.vi"/>
																	<Item Name="get_pick_line_node_term.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/GetNodeTerm/StringProcessingNode/Methods/get_pick_line_node_term.vi"/>
																</Item>
																<Item Name="TypeDefinitions" Type="Folder">
																	<Item Name="string_node_type.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/GetNodeTerm/StringProcessingNode/TypeDefinitions/string_node_type.ctl"/>
																</Item>
															</Item>
														</Item>
														<Item Name="PolishCodes" Type="Folder">
															<Item Name="Interface" Type="Folder">
																<Item Name="polish.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Interface/polish.vi"/>
															</Item>
															<Item Name="Internal" Type="Folder">
																<Item Name="clear_specific_error.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Internal/clear_specific_error.vi"/>
															</Item>
															<Item Name="Methods" Type="Folder">
																<Item Name="add_default_value_on_label.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Methods/add_default_value_on_label.vi"/>
																<Item Name="bd_bounds.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Methods/bd_bounds.vi"/>
																<Item Name="bd_terminal_label_position.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Methods/bd_terminal_label_position.vi"/>
																<Item Name="control_label_font.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Methods/control_label_font.vi"/>
																<Item Name="control_label_transparent.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Methods/control_label_transparent.vi"/>
																<Item Name="rearrange_controls.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Methods/rearrange_controls.vi"/>
																<Item Name="ring_digital_visible.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Methods/ring_digital_visible.vi"/>
																<Item Name="save_vi.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Methods/save_vi.vi"/>
																<Item Name="visa_resource_name_required.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/PolishCodes/Methods/visa_resource_name_required.vi"/>
															</Item>
														</Item>
														<Item Name="add_string_constant.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/add_string_constant.vi"/>
														<Item Name="find_existing_controls.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/find_existing_controls.vi"/>
														<Item Name="find_term_objects_pos_and_refs.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Iternl/find_term_objects_pos_and_refs.vi"/>
													</Item>
													<Item Name="Misc" Type="Folder">
														<Item Name="add_percentage_for_floating_datatype.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Misc/add_percentage_for_floating_datatype.vi"/>
														<Item Name="build_paths.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Misc/build_paths.vi"/>
														<Item Name="cal_max_min_y.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Misc/cal_max_min_y.vi"/>
														<Item Name="cal_multilines_heights_and_widths.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Misc/cal_multilines_heights_and_widths.vi"/>
														<Item Name="close_refs.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Misc/close_refs.vi"/>
														<Item Name="use_pick_line_or_format_stirng.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Misc/use_pick_line_or_format_stirng.vi"/>
													</Item>
													<Item Name="Mth" Type="Folder">
														<Item Name="AddInstrumentInterface" Type="Folder">
															<Item Name="add_visa_in_error_in.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Mth/AddInstrumentInterface/add_visa_in_error_in.vi"/>
															<Item Name="add_visa_out_error_out.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Mth/AddInstrumentInterface/add_visa_out_error_out.vi"/>
															<Item Name="connect_visa_write_wires.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Mth/AddInstrumentInterface/connect_visa_write_wires.vi"/>
														</Item>
														<Item Name="AddOneCommandCodes" Type="Folder">
															<Item Name="add_multi_controls_command.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Mth/AddOneCommandCodes/add_multi_controls_command.vi"/>
															<Item Name="add_one_control_command.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Mth/AddOneCommandCodes/add_one_control_command.vi"/>
															<Item Name="add_only_string_on_bd.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Mth/AddOneCommandCodes/add_only_string_on_bd.vi"/>
														</Item>
														<Item Name="add_instrument_interface.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Mth/add_instrument_interface.vi"/>
														<Item Name="add_one_command_codes.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/Mth/add_one_command_codes.vi"/>
													</Item>
													<Item Name="TypeDefinitions" Type="Folder">
														<Item Name="boolean.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/boolean.ctl"/>
														<Item Name="control_class.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/control_class.ctl"/>
														<Item Name="control_data_type.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/control_data_type.ctl"/>
														<Item Name="error_in.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/error_in.ctl"/>
														<Item Name="error_out.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/error_out.ctl"/>
														<Item Name="ring_string_and_value.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/ring_string_and_value.ctl"/>
														<Item Name="single_cmd_spec.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/single_cmd_spec.ctl"/>
														<Item Name="single_control_spec.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/single_control_spec.ctl"/>
														<Item Name="single_vi_spec.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/single_vi_spec.ctl"/>
														<Item Name="vi_type.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/vi_type.ctl"/>
														<Item Name="visa_resource_name_in.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/visa_resource_name_in.ctl"/>
														<Item Name="visa_resource_name_out.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Intf/GenStdVI/Mth/GenOneStdVI/TypeDefinitions/visa_resource_name_out.ctl"/>
													</Item>
												</Item>
											</Item>
										</Item>
									</Item>
									<Item Name="Misc" Type="Folder">
										<Item Name="AddNode" Type="Folder">
											<Item Name="Interface" Type="Folder">
												<Item Name="add_node.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Interface/add_node.vi"/>
											</Item>
											<Item Name="Internal" Type="Folder">
												<Item Name="add_function.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Internal/add_function.vi"/>
											</Item>
											<Item Name="Methods" Type="Folder">
												<Item Name="add_boolean_node.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Methods/add_boolean_node.vi"/>
												<Item Name="add_concatenate_strings_node.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Methods/add_concatenate_strings_node.vi"/>
												<Item Name="add_format_into_string_node.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Methods/add_format_into_string_node.vi"/>
												<Item Name="add_pick_line_node.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Methods/add_pick_line_node.vi"/>
												<Item Name="add_scan_from_string_node.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Methods/add_scan_from_string_node.vi"/>
												<Item Name="add_spreadsheet_string_to_array.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Methods/add_spreadsheet_string_to_array.vi"/>
												<Item Name="add_subVI_node.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Methods/add_subVI_node.vi"/>
												<Item Name="add_visa_read_node.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Methods/add_visa_read_node.vi"/>
												<Item Name="add_visa_write_node.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/Methods/add_visa_write_node.vi"/>
											</Item>
											<Item Name="TypeDefinitions" Type="Folder">
												<Item Name="node_types.ctl" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/AddNode/TypeDefinitions/node_types.ctl"/>
											</Item>
										</Item>
										<Item Name="adjust_position.vi" Type="VI" URL="../express/Utility/StudioHelper/Gtor/Mth/GenVI/Misc/adjust_position.vi"/>
									</Item>
								</Item>
							</Item>
						</Item>
					</Item>
					<Item Name="auto_gen_logic.vi" Type="VI" URL="../express/Utility/auto_gen_logic.vi"/>
					<Item Name="check_duplicate.vi" Type="VI" URL="../express/Utility/check_duplicate.vi"/>
					<Item Name="command_spec.ctl" Type="VI" URL="../express/Utility/command_spec.ctl"/>
					<Item Name="fill_tree.vi" Type="VI" URL="../express/Utility/fill_tree.vi"/>
					<Item Name="find_terms_by_names.vi" Type="VI" URL="../express/Utility/find_terms_by_names.vi"/>
					<Item Name="gen_logic_vi_with_cmd_array.vi" Type="VI" URL="../express/Utility/gen_logic_vi_with_cmd_array.vi"/>
					<Item Name="gen_node.vi" Type="VI" URL="../express/Utility/gen_node.vi"/>
					<Item Name="generate_block_data_array.vi" Type="VI" URL="../express/Utility/generate_block_data_array.vi"/>
					<Item Name="parse_cmd_from_file.vi" Type="VI" URL="../express/Utility/parse_cmd_from_file.vi"/>
					<Item Name="pop_dialog.vi" Type="VI" URL="../express/Utility/pop_dialog.vi"/>
					<Item Name="pop_dialog_if_no_duplicate.vi" Type="VI" URL="../express/Utility/pop_dialog_if_no_duplicate.vi"/>
					<Item Name="remove_empty_group.vi" Type="VI" URL="../express/Utility/remove_empty_group.vi"/>
					<Item Name="show_match_items.vi" Type="VI" URL="../express/Utility/show_match_items.vi"/>
					<Item Name="sort_property.vi" Type="VI" URL="../express/Utility/sort_property.vi"/>
					<Item Name="split_str_array.vi" Type="VI" URL="../express/Utility/split_str_array.vi"/>
					<Item Name="sub_replace_self.vi" Type="VI" URL="../express/Utility/sub_replace_self.vi"/>
					<Item Name="update_array_data_and_list_view.vi" Type="VI" URL="../express/Utility/update_array_data_and_list_view.vi"/>
					<Item Name="update_enum_string_with_cmd_info.vi" Type="VI" URL="../express/Utility/update_enum_string_with_cmd_info.vi"/>
					<Item Name="update_mapid.vi" Type="VI" URL="../express/Utility/update_mapid.vi"/>
					<Item Name="update_two_array_attribute_cmdlist.vi" Type="VI" URL="../express/Utility/update_two_array_attribute_cmdlist.vi"/>
					<Item Name="update_two_attribute_cmdlist.vi" Type="VI" URL="../express/Utility/update_two_attribute_cmdlist.vi"/>
				</Item>
				<Item Name="CommandList.xml" Type="Document" URL="../express/CommandList.xml"/>
				<Item Name="Express.aliases" Type="Document" URL="../express/Express.aliases"/>
				<Item Name="Express.lvlps" Type="Document" URL="../express/Express.lvlps"/>
				<Item Name="Express.lvproj" Type="Document" URL="../express/Express.lvproj"/>
				<Item Name="SCPI Node.xnode" Type="XNode" URL="../express/SCPI Node.xnode"/>
				<Item Name="xnode_to_terms.vi" Type="VI" URL="../express/xnode_to_terms.vi"/>
			</Item>
			<Item Name="Manuals" Type="Folder">
				<Item Name="9018-03690(PROG).pdf" Type="Document" URL="../Manuals/9018-03690(PROG).pdf"/>
			</Item>
			<Item Name="Private" Type="Folder"/>
			<Item Name="Public" Type="Folder">
				<Item Name="Action-Status" Type="Folder">
					<Item Name="Action-Status.mnu" Type="Document" URL="../Public/Action-Status/Action-Status.mnu"/>
				</Item>
				<Item Name="Configure" Type="Folder">
					<Item Name="Bit Error Rate Test" Type="Folder">
						<Item Name="Bit Error Rate Test.mnu" Type="Document" URL="../Public/Configure/Bit Error Rate Test/Bit Error Rate Test.mnu"/>
					</Item>
					<Item Name="Digital Signal Interface" Type="Folder">
						<Item Name="Digital Input Signal" Type="Folder">
							<Item Name="Digital Input Signal.mnu" Type="Document" URL="../Public/Configure/Digital Signal Interface/Digital Input Signal/Digital Input Signal.mnu"/>
						</Item>
						<Item Name="Digital Output Signal" Type="Folder">
							<Item Name="Digital Output Signal.mnu" Type="Document" URL="../Public/Configure/Digital Signal Interface/Digital Output Signal/Digital Output Signal.mnu"/>
						</Item>
						<Item Name="Digital Signal Interface.mnu" Type="Document" URL="../Public/Configure/Digital Signal Interface/Digital Signal Interface.mnu"/>
					</Item>
					<Item Name="Modulation" Type="Folder">
						<Item Name="AWGN ARB" Type="Folder">
							<Item Name="AWGN ARB.mnu" Type="Document" URL="../Public/Configure/Modulation/AWGN ARB/AWGN ARB.mnu"/>
						</Item>
						<Item Name="AWGN Real-Time" Type="Folder">
							<Item Name="AWGN Real-Time.mnu" Type="Document" URL="../Public/Configure/Modulation/AWGN Real-Time/AWGN Real-Time.mnu"/>
						</Item>
						<Item Name="Custom Modulation" Type="Folder">
							<Item Name="Custom Modulation.mnu" Type="Document" URL="../Public/Configure/Modulation/Custom Modulation/Custom Modulation.mnu"/>
						</Item>
						<Item Name="Custom Real-Time" Type="Folder">
							<Item Name="Custom Real-Time.mnu" Type="Document" URL="../Public/Configure/Modulation/Custom Real-Time/Custom Real-Time.mnu"/>
						</Item>
						<Item Name="Digital Modulation" Type="Folder">
							<Item Name="Digital Modulation.mnu" Type="Document" URL="../Public/Configure/Modulation/Digital Modulation/Digital Modulation.mnu"/>
						</Item>
						<Item Name="Dual ARB" Type="Folder">
							<Item Name="Dual ARB.mnu" Type="Document" URL="../Public/Configure/Modulation/Dual ARB/Dual ARB.mnu"/>
						</Item>
						<Item Name="Dual Modulation" Type="Folder">
							<Item Name="Dual Modulation.mnu" Type="Document" URL="../Public/Configure/Modulation/Dual Modulation/Dual Modulation.mnu"/>
						</Item>
						<Item Name="Two Tone And Multitone" Type="Folder">
							<Item Name="Two Tone And Multitone.mnu" Type="Document" URL="../Public/Configure/Modulation/Two Tone And Multitone/Two Tone And Multitone.mnu"/>
						</Item>
						<Item Name="Vector Modulation" Type="Folder">
							<Item Name="Vector Modulation.mnu" Type="Document" URL="../Public/Configure/Modulation/Vector Modulation/Vector Modulation.mnu"/>
						</Item>
						<Item Name="Modulation.mnu" Type="Document" URL="../Public/Configure/Modulation/Modulation.mnu"/>
					</Item>
					<Item Name="Configure.mnu" Type="Document" URL="../Public/Configure/Configure.mnu"/>
				</Item>
				<Item Name="Data" Type="Folder">
					<Item Name="Data.mnu" Type="Document" URL="../Public/Data/Data.mnu"/>
				</Item>
				<Item Name="Obsolete" Type="Folder"/>
				<Item Name="User Flatness" Type="Folder">
					<Item Name="Flatness-SetupFrequency.vi" Type="VI" URL="../Public/User Flatness/Flatness-SetupFrequency.vi"/>
					<Item Name="Flatness_Load-CalFromStep.vi" Type="VI" URL="../Public/User Flatness/Flatness_Load-CalFromStep.vi"/>
					<Item Name="Flatness_Load-Pairs.vi" Type="VI" URL="../Public/User Flatness/Flatness_Load-Pairs.vi"/>
					<Item Name="Flatness_ON-OFF.vi" Type="VI" URL="../Public/User Flatness/Flatness_ON-OFF.vi"/>
					<Item Name="Flatness_PreSet.vi" Type="VI" URL="../Public/User Flatness/Flatness_PreSet.vi"/>
				</Item>
				<Item Name="Utility" Type="Folder">
					<Item Name="Utility.mnu" Type="Document" URL="../Public/Utility/Utility.mnu"/>
				</Item>
				<Item Name="dir.mnu" Type="Document" URL="../Public/dir.mnu"/>
			</Item>
			<Item Name="Agilent PSG MXG Series Readme.html" Type="Document" URL="../Agilent PSG MXG Series Readme.html"/>
			<Item Name="Agilent PSG MXG Series.aliases" Type="Document" URL="../Agilent PSG MXG Series.aliases"/>
			<Item Name="Agilent PSG MXG Series.lvlib" Type="Library" URL="../Agilent PSG MXG Series.lvlib"/>
			<Item Name="Agilent PSG MXG Series.lvlps" Type="Document" URL="../Agilent PSG MXG Series.lvlps"/>
		</Item>
		<Item Name="Agilent PSG MXG Series.bin3" Type="Document" URL="/&lt;instrlib&gt;/Agilent PSG MXG Series/Examples/Agilent PSG MXG Series.bin3"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
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
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="compatReadText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatReadText.vi"/>
				<Item Name="Read File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read File+ (string).vi"/>
				<Item Name="Open File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Open File+.vi"/>
				<Item Name="Read Lines From File (with error IO).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Lines From File (with error IO).vi"/>
				<Item Name="Read Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (string).vi"/>
				<Item Name="Read Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (I64).vi"/>
				<Item Name="Read Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Read Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet.vi"/>
			</Item>
			<Item Name="VISA_OPC.vi" Type="VI" URL="../../VISA_OPC.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
