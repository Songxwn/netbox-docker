# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins
PLUGINS = ['netbox_qrcode', 'netbox_ipcalculator']

# Plugins configuration settings. These settings are used by various plugins that the user may have installed.
# Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.
PLUGINS_CONFIG = {
    'netbox_qrcode': {
        'with_text': True,
        'text_fields': ['name', 'serial'],
        'font': 'SourceHanSansSC',
        'custom_text': '所属： Songxwn.com',
        'text_location': 'right',
        'qr_version': 1,
        'qr_error_correction': 0,
        'qr_box_size': 6,
        'qr_border': 4,
        # per object options
        'cable': None,  # disable QR code for Cable object
        'rack': {
            'text_template': '{{ obj.name }}\n租户: {{ obj.tenant }}\n站点: {{ obj.site }}',
            'qr_box_size': 6,
            'custom_text': None,
        },
        'device': {
            'text_template': '{{ obj.name }}\n带外管理IP: {{ obj.oob_ip }}\n主IPv4地址: {{ obj.primary_ip }}\n序列号: {{ obj.serial }}\n位置: {{ obj.location }}\n机柜: {{ obj.rack }} - U位: {{ obj.position }}',
            
            'qr_box_size': 6,
            'custom_text': None,
        }
    }
}
