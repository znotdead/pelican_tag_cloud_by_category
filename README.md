Pelican tag cloud by category
=============================


Plugin for pelican to display tags in tag cloud only for selected category.

1. Install plugin as it written on Pelican docs.

*Example:*

**pelicanconf.py**
```python
PLUGIN_PATHS = ['../pelican_tag_cloud_by_category/',]
PLUGINS = ['tag_cloud_by_category', ]

DISPLAY_TAGS_FOR_CATEGORY = True
```
**DISPLAY_TAGS_INLINE** option also available.

2. Setup your templates.

Download [my pelican-bootstrap3 theme](https://github.com/znotdead/pelican-bootstrap3)
or customize your own.

*Example:*

***includes/sidebar.html***
```
  {% if DISPLAY_TAGS_ON_SIDEBAR %}
    {% if DISPLAY_TAGS_FOR_CATEGORY and category %}
        {% for cat, cat_tags in tag_cloud_by_category %}
          {% if category == cat %}
            {% set tag_cloud = cat_tags %}
            {% include 'includes/tag_cloud.html' %}
          {% endif %}
        {% endfor %}
    {% else %}
      {% include 'includes/tag_cloud.html' %}
    {% endif %}
  {% endif %}
```

**includes/tag_cloud.html**
```
{% if DISPLAY_TAGS_INLINE %}
    {% set tags = tag_cloud | sort(attribute='0') %}
{% else %}
    {% set tags = tag_cloud | sort(attribute='1') %}
{% endif %}

<li class="list-group-item"><a href="{{ SITEURL }}/{{ TAGS_URL }}"><h4><i class="fa fa-tags fa-lg"></i><span class="icon-label">Tags</span></h4></a>
    <ul class="list-group {% if DISPLAY_TAGS_INLINE %}list-inline tagcloud{% endif %}" id="tags">

    {% for tag in tags %}
        <li class="list-group-item tag-{{ tag.1 }}">
            <a href="{{ SITEURL }}/{{ tag.0.url }}">
                {{ tag.0 }}
            </a>
        </li>
    {% endfor %}
    </ul>
</li>
```
