# Events
EVENT_CREATE = 'create'
EVENT_UPDATE = 'update'
EVENT_DELETE = 'delete'
EVENT_JOB_START = 'job_start'
EVENT_JOB_END = 'job_end'


# Webhooks
HTTP_CONTENT_TYPE_JSON = 'application/json'

WEBHOOK_EVENT_TYPES = {
    EVENT_CREATE: 'created',
    EVENT_UPDATE: 'updated',
    EVENT_DELETE: 'deleted',
    EVENT_JOB_START: 'job_started',
    EVENT_JOB_END: 'job_ended',
}

# Dashboard
DEFAULT_DASHBOARD = [
    {
        'widget': 'extras.BookmarksWidget',
        'width': 4,
        'height': 5,
        'title': '书签',
        'color': 'orange',
    },
    {
        'widget': 'extras.ObjectCountsWidget',
        'width': 4,
        'height': 2,
        'title': '组织架构',
        'config': {
            'models': [
                'dcim.site',
                'tenancy.tenant',
                'tenancy.contact',
            ]
        }
    },
    {
        'widget': 'extras.NoteWidget',
        'width': 4,
        'height': 2,
        'title': 'NetBox中文社区微信群',
        'color': 'green',
        'config': {
            'content': (
                '可发送微信号到邮箱➡️ me@songxwn.com'
            )
        }
    },
    {
        'widget': 'extras.ObjectCountsWidget',
        'width': 4,
        'height': 3,
        'title': 'IP地址管理',
        'config': {
            'models': [
                'ipam.vrf',
                'ipam.aggregate',
                'ipam.prefix',
                'ipam.iprange',
                'ipam.ipaddress',
                'ipam.vlan',
            ]
        }
    },
    {
        'widget': 'extras.RSSFeedWidget',
        'width': 4,
        'height': 5,
        'title': '个人博客',
        'config': {
            'feed_url': 'https://songxwn.com/atom.xml',
            'max_entries': 20,
            'cache_timeout': 14400,
        }
    },
    {
        'widget': 'extras.ObjectCountsWidget',
        'width': 4,
        'height': 3,
        'title': '运营商传输线路',
        'config': {
            'models': [
                'circuits.provider',
                'circuits.circuit',
                'circuits.providernetwork',
                'circuits.provideraccount',
            ]
        }
    },
    {
        'widget': 'extras.ObjectCountsWidget',
        'width': 4,
        'height': 3,
        'title': 'DCIM',
        'config': {
            'models': [
                'dcim.site',
                'dcim.rack',
                'dcim.devicetype',
                'dcim.device',
                'dcim.cable',
            ],
        }
    },
    {
        'widget': 'extras.ObjectCountsWidget',
        'width': 4,
        'height': 2,
        'title': '虚拟化',
        'config': {
            'models': [
                'virtualization.cluster',
                'virtualization.virtualmachine',
            ]
        }
    },
    {
        'widget': 'extras.ObjectListWidget',
        'width': 12,
        'height': 5,
        'title': '操作日志',
        'color': 'blue',
        'config': {
            'model': 'extras.objectchange',
            'page_size': 25,
        }
    },
]
