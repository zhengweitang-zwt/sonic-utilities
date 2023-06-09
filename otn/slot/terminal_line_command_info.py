LOGICAL_CHANNEL = "LOGICAL_CHANNEL"
TRANSCEIVER     = "TRANSCEIVER"
OTN             = "OTN"
PORT            = "PORT"
OCH             = "OCH"

MODULE_LIST = [
    {'Module': LOGICAL_CHANNEL,             'Field': 'transceiver',                             'show_name': 'Name'},
    {'Module': TRANSCEIVER, 				'Field': 'present', 					            'show_name': 'LineExist'},
    {'Module': TRANSCEIVER, 				'Field': 'vendor', 					                'show_name': 'ModuleVendor'},
    {'Module': TRANSCEIVER, 				'Field': 'hardware-version', 			            'show_name': 'ModuleHardversion'},
    {'Module': TRANSCEIVER, 				'Field': 'mfg-date', 					            'show_name': 'ModuleManudate'},
    {'Module': TRANSCEIVER, 				'Field': 'serial-no', 					            'show_name': 'ModuleSn'},
    {'Module': TRANSCEIVER, 				'Field': 'firmware-version', 			            'show_name': 'ModuleFirmwareVersion'},
    {'Module': TRANSCEIVER, 				'Field': 'laser-age', 					            'show_name': 'ModuleLaserAge'},
    {'Module': TRANSCEIVER, 				'Field': 'operate-time', 			                'show_name': 'ModuleOperateTime(h)'},
    {'Module': TRANSCEIVER, 				'Field': 'part-no', 					            'show_name': 'ModulePartNumber'},
    {'Module': OCH,                         'Field': 'frequency',                               'show_name': 'ModuleFreq(MHz)'},
    {'Module': TRANSCEIVER, 				'Field': 'frequency-range', 			            'show_name': 'ModuleFreqRange'},
    {'Module': TRANSCEIVER, 				'Field': 'instant', 					            'show_name': 'ModuleVoltage(W)'},
    {'Module': TRANSCEIVER, 				'Field': 'oui', 					                'show_name': 'ModuleOUI'},
    {'Module': TRANSCEIVER, 				'Field': 'power-class', 				            'show_name': 'ModulePowerClass'},
    {'Module': TRANSCEIVER, 				'Field': 'newwork-bit-rate', 			            'show_name': 'ModuleMaxNetworkBitRate(Gbps)'},
    {'Module': TRANSCEIVER, 				'Field': 'host-bit-rate', 				            'show_name': 'ModuleMaxHostBitRate(Gbps)'},
    {'Module': TRANSCEIVER, 				'Field': 'sm-fiber-len', 				            'show_name': 'ModuleMaxsigmodefbrlen(KM)'},
    {'Module': TRANSCEIVER, 				'Field': 'mm-fiber-len', 				            'show_name': 'ModuleMaxmultmodefbrlen(KM)'},
    {'Module': TRANSCEIVER, 				'Field': 'copper-cable-len', 			            'show_name': 'ModuleMaxcoppercablelen(M)'},
    {'Module': TRANSCEIVER, 				'Field': 'max-wavelength', 				            'show_name': 'ModuleMaxwavelength(PM)'},
    {'Module': TRANSCEIVER, 				'Field': 'min-wavelength', 				            'show_name': 'ModuleMinwavelength(PM)'},
    {'Module': TRANSCEIVER, 				'Field': 'max-tx-power', 				            'show_name': 'ModuleMaxtxpwr(uW)'},
    {'Module': TRANSCEIVER, 				'Field': 'max-rx-power', 				            'show_name': 'ModuleMaxrxpwr(uW)'},
    {'Module': TRANSCEIVER, 				'Field': 'max-oper-temp', 				            'show_name': 'ModuleMaxopertemp(C)'},
    {'Module': TRANSCEIVER, 				'Field': 'min-oper-temp', 				            'show_name': 'ModuleMinopertemp(C)'},
    {'Module': TRANSCEIVER, 				'Field': 'vcc-high-alarm-threshold', 	            'show_name': 'ModuleVcchighalarmthreshold(mV)'},
    {'Module': TRANSCEIVER, 				'Field': 'vcc-high-warn-threshold', 	            'show_name': 'ModuleVcchighwarnthreshold(mV)'},
    {'Module': TRANSCEIVER, 				'Field': 'vcc-low-alarm-threshold', 	            'show_name': 'ModuleVcclowalarmthreshold(mV)'},
    {'Module': TRANSCEIVER, 				'Field': 'vcc-low-warn-threshold', 					'show_name': 'ModuleVcclowwarnthreshold(mV)'},
    {'Module': TRANSCEIVER, 				'Field': 'rx-total-power-high-alarm-threshold', 	'show_name': 'ModuleRxtotalpwrhighalarmthreshold(dBm)'},
    {'Module': TRANSCEIVER, 				'Field': 'rx-total-power-high-warn-threshold', 		'show_name': 'ModuleRxtotalpwrhighwarnthreshold(dBm)'},
    {'Module': TRANSCEIVER, 				'Field': 'rx-total-power-low-alarm-threshold', 		'show_name': 'ModuleRxtotalpwrlowalarmthreshold(dBm)'},
    {'Module': TRANSCEIVER, 				'Field': 'rx-total-power-low-warn-threshold', 		'show_name': 'ModuleRxtotalpwrlowwarnthreshold(dBm)'},
    {'Module': TRANSCEIVER, 				'Field': 'oa-pump-current-high-alarm-threshold', 	'show_name': 'ModuleOapumpcurrenthighalarmthreshold(mA)'},
    {'Module': TRANSCEIVER, 				'Field': 'oa-pump-current-high-warn-threshold', 	'show_name': 'ModuleOapumpcurrenthighwarnthreshold(mA)'},
    {'Module': TRANSCEIVER, 				'Field': 'oa-pump-current-low-alarm-threshold', 	'show_name': 'ModuleOapumpcurrentlowalarmthreshold(mA)'},
    {'Module': TRANSCEIVER, 				'Field': 'oa-pump-current-low-warn-threshold', 		'show_name': 'ModuleOapumpcurrentlowwarnthreshold(mA)'},
    {'Module': TRANSCEIVER, 				'Field': 'tx-bais-high-alarm-threshold', 			'show_name': 'ModuleTxbiashighalarmthreshold(mA)'},
    {'Module': TRANSCEIVER, 				'Field': 'tx-bais-high-warn-threshold', 			'show_name': 'ModuleTxbiashighwarnthreshold(mA)'},
    {'Module': TRANSCEIVER, 				'Field': 'tx-bais-low-alarm-threshold', 			'show_name': 'ModuleTxbiaslowalarmthreshold(mA)'},
    {'Module': TRANSCEIVER, 				'Field': 'tx-bais-low-warn-threshold', 				'show_name': 'ModuleTxbiaslowwarnthreshold(mA)'},    
]

STATE_LIST = [
    {'Module': LOGICAL_CHANNEL,         'Field': 'transceiver',             'show_name': 'Name'},
    {'Module': PORT, 					'Field': 'oper-status', 			'show_name': 'PortOperState'},
    {'Module': LOGICAL_CHANNEL, 		'Field': 'admin-state', 			'show_name': 'PortAdministate'},
    {'Module': TRANSCEIVER, 			'Field': 'vendor-expect', 			'show_name': 'DcoVendorPreconf'},
    {'Module': TRANSCEIVER, 			'Field': 'enabled', 				'show_name': 'tx-laser'},
    {'Module': LOGICAL_CHANNEL, 		'Field': 'loopback-mode', 			'show_name': 'LineLoop'},
    {'Module': LOGICAL_CHANNEL, 		'Field': 'tx-test-signal-pattern', 	'show_name': 'LinePrbsTx'},
    {'Module': LOGICAL_CHANNEL, 		'Field': 'rx-test-signal-pattern', 	'show_name': 'LinePrbsRx'},
    {'Module': OTN, 					'Field': 'maintenance', 			'show_name': 'LineForceInsert'},
    {'Module': OTN, 					'Field': 'tti-msg-auto', 			'show_name': 'tti-msg-auto-mode'},
    {'Module': OTN, 					'Field': 'tti-msg-transmit', 		'show_name': 'Tti_transmit'},
    {'Module': OTN, 					'Field': 'tti-msg-expected', 		'show_name': 'Tti_rx_expected'},
    {'Module': OCH, 					'Field': 'target-output-power',		'show_name': 'TxPower(dBm)'},
    {'Module': OCH, 					'Field': 'frequency',				'show_name': 'Frequency(MHz)'},
    {'Module': OCH, 					'Field': 'operational-mode',		'show_name': 'OperationlMode'},
    {'Module': OTN, 					'Field': 'tti-msg-recv', 			'show_name': 'Tti_rx'},
    {'Module': TRANSCEIVER, 			'Field': 'enabled', 				'show_name': 'LineState'},
    {'Module': TRANSCEIVER, 			'Field': 'present', 				'show_name': 'LineExist'},
    {'Module': OCH, 					'Field': 'frequency', 				'show_name': 'LineFrequency(MHz)'},
    {'Module': LOGICAL_CHANNEL, 		'Field': 'tx-test-signal-pattern', 	'show_name': 'LinePrbsStateTx'},
    {'Module': LOGICAL_CHANNEL, 		'Field': 'rx-test-signal-pattern', 	'show_name': 'LinePrbsStateRx'},
    {'Module': PORT, 					'Field': 'led-color', 				'show_name': 'LedState'},
]
 
CONFIG_LIST = [
    {'Module': LOGICAL_CHANNEL,   'Field': 'transceiver',               'show_name': 'Name'},
    {'Module': LOGICAL_CHANNEL, 	'Field': 'admin-state', 			'show_name': 'PortAdminstate'},
    {'Module': PORT, 				'Field': 'cd-range-lower', 			'show_name': 'RxCdRangeLow(ps/nm)'},
    {'Module': PORT, 				'Field': 'cd-range-upper', 			'show_name': 'RxCdRangeHigh(ps/nm)'},
    {'Module': TRANSCEIVER, 		'Field': 'vendor-expect', 			'show_name': 'DcoVendorPreconf'},
    {'Module': TRANSCEIVER, 		'Field': 'enabled', 			    'show_name': 'tx-laser'},
    {'Module': LOGICAL_CHANNEL, 	'Field': 'loopback-mode', 			'show_name': 'LineLoop'},
    {'Module': LOGICAL_CHANNEL, 	'Field': 'tx-test-signal-pattern', 	'show_name': 'LinePrbsTx'},
    {'Module': LOGICAL_CHANNEL, 	'Field': 'rx-test-signal-pattern', 	'show_name': 'LinePrbsRx(ms)'},
    {'Module': OTN, 				'Field': 'maintenance', 			'show_name': 'LineForceInsert'},
    {'Module': OTN, 				'Field': 'tti-msg-auto', 			'show_name': 'tti-msg-auto-mode'},
    {'Module': OTN, 				'Field': 'tti-msg-transmit', 	    'show_name': 'Tti_transmit'},
    {'Module': OTN, 				'Field': 'tti-msg-expected', 	    'show_name': 'Tti_rx_expected'},
    {'Module': OCH, 				'Field': 'target-output-power',	    'show_name': 'TxPower(dBm)'},
    {'Module': OCH, 				'Field': 'frequency',			    'show_name': 'Frequency(MHz)'},
    {'Module': OCH, 				'Field': 'operational-mode',		'show_name': 'OperationlMode'},
]


PM_LIST = [
    {'Module': TRANSCEIVER, 	'Field': 'InputPower', 						            'show_name': 'InputPower(dBm)'},
    {'Module': TRANSCEIVER, 	'Field': 'OutputPower', 						        'show_name': 'OutputPower(dBm)'},
    {'Module': TRANSCEIVER, 	'Field': 'LaserBiasCurrent', 						    'show_name': 'LaserBias(mA)'},
    {'Module': TRANSCEIVER, 	'Field': 'PowerConsumption', 						    'show_name': 'PowerConsumption(W)'},
    {'Module': TRANSCEIVER, 	'Field': 'CaseTemperature', 						    'show_name': 'CaseTemp(C)'},
    {'Module': TRANSCEIVER, 	'Field': 'Temperature', 						        'show_name': 'LaserTemp(C)'},
    {'Module': TRANSCEIVER, 	'Field': 'TxModBiasXi', 						        'show_name': 'TX MOD BIAS X/I'},
    {'Module': TRANSCEIVER, 	'Field': 'TxModBiasXq', 						        'show_name': 'TX MOD BIAS X/Q'},
    {'Module': TRANSCEIVER, 	'Field': 'TxModBiasYi', 						        'show_name': 'TX MOD BIAS Y/I'},
    {'Module': TRANSCEIVER, 	'Field': 'TxModBiasYq', 						        'show_name': 'TX MOD BIAS Y/Q'},
    {'Module': TRANSCEIVER, 	'Field': 'TxModBiasXph', 						        'show_name': 'TX MOD BIAS X/PH'},
    {'Module': TRANSCEIVER, 	'Field': 'TxModBiasYph', 						        'show_name': 'TX MOD BIAS Y/PH'},
    {'Module': OTN, 			'Field': 'QValue', 						                'show_name': 'Q-Factor'},
    {'Module': OTN, 			'Field': 'Esnr', 						                'show_name': 'ESNR'},
    {'Module': OTN, 			'Field': 'PreFecBer', 						            'show_name': 'PRE-FEC-BER'},
    {'Module': OTN, 			'Field': 'PostFecBer', 						            'show_name': 'POST-FEC-BER'},
    {'Module': OCH, 			'Field': 'Osnr', 						                'show_name': 'OSNR(dB)'},
    {'Module': OCH, 			'Field': 'ChromaticDispersion', 		                'show_name': 'CD(ps/nm)'},
    {'Module': OCH, 			'Field': 'PolarizationDependentLoss', 	                'show_name': 'PDL(dB)'},
    {'Module': OCH, 			'Field': 'ActualFrequencyOffset', 		                'show_name': 'FOFF(MHz)'},
    {'Module': OCH, 			'Field': 'GroupDelay', 					                'show_name': 'DGD(ps)'},
    {'Module': OCH, 			'Field': 'SecondOrderPolarizationModeDispersion', 		'show_name': 'SoPMD(ps^2)'},
    {'Module': OCH, 			'Field': 'SopChangeRate', 						        'show_name': 'SOP CHANGE RATE(rad/s)'},
    {'Module': OCH, 			'Field': 'LaserBiasCurrent', 						    'show_name': 'LASER BIAS(mA)'},
    {'Module': OCH, 			'Field': 'EdfaBiasCurrent', 						    'show_name': 'EDFA BIAS(mA)'},
    {'Module': OCH, 			'Field': 'InputSignalPower', 						    'show_name': 'Signal Input Power(dBm)'},
]

OTU_PM_LIST = [
    {'Module': TRANSCEIVER, 'Field': 'loss-time', 				        'show_name': 'LossTime(s)'},
    {'Module': OTN,         'Field': 'fec-corrected-bits', 			    'show_name': 'BE-FEC'},
    {'Module': OTN,         'Field': 'fec-uncorrectable-blocks', 		'show_name': 'UBLE-FEC'},
    {'Module': OTN,         'Field': 'errored-blocks', 				    'show_name': 'EB'},
    {'Module': OTN,         'Field': 'sm-bei', 				            'show_name': 'EBI count'},
    {'Module': OTN,         'Field': 'background-block-errors', 		'show_name': 'BBE'},
    {'Module': OTN,         'Field': 'severely-errored-seconds', 		'show_name': 'SES(s)'},
    {'Module': OTN,         'Field': 'errored-seconds', 				'show_name': 'ES(s)'},
    {'Module': OTN,         'Field': 'unavailable-seconds', 			'show_name': 'UAS(s)'},
    {'Module': OTN,         'Field': 'code-violations', 				'show_name': 'CV'},
]