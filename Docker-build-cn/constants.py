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
        'title': 'Bookmarks',
        'color': 'orange',
    },
    {
        'widget': 'extras.ObjectCountsWidget',
        'width': 4,
        'height': 2,
        'title': 'Organization',
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
        'title': 'IPAM',
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
        'height': 4,
        'title': '个人博客',
        'config': {
            'feed_url': 'https://songxwn.com/atom.xml',
            'max_entries': 15,
            'cache_timeout': 14400,
        }
    },
    {
        'widget': 'extras.ObjectCountsWidget',
        'width': 4,
        'height': 3,
        'title': 'Circuits',
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
        'title': 'Virtualization',
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
        'title': 'Change Log',
        'color': 'blue',
        'config': {
            'model': 'extras.objectchange',
            'page_size': 25,
        }
    },
]
