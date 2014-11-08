#-*- coding: utf-8 -*-
import math
import random

from collections import defaultdict
from operator import itemgetter

from pelican import signals

def tags_by_category(sender):
    max_items = sender.settings.get('TAG_CLOUD_MAX_ITEMS')
    steps = sender.settings.get('TAG_CLOUD_STEPS')

    tag_cloud_by_category = defaultdict()
    categories = [l[0] for l in sender.categories]
    for category in categories:
        tag_cloud_by_category[category] = defaultdict(int)

    # create tag cloud
    for article in sender.articles:
        for tag in getattr(article, 'tags', []):
            tag_cloud_by_category[article.category][tag] += 1

    for category, category_tag_cloud in tag_cloud_by_category.items():
        tag_cloud_by_category[category] = sorted(category_tag_cloud.items(),
                                                 key=itemgetter(1), reverse=True)

        tag_cloud_by_category[category] = tag_cloud_by_category[category][:max_items]

    tags_category = {}
    tag_cloud = {}
    for category in tag_cloud_by_category.keys():
        tags_category[category] = list(map(itemgetter(1), tag_cloud_by_category[category]))

        if tags_category[category]:
            max_count = max(tags_category[category])

        # calculate word sizes
        tag_cloud[category] = [
            (
                tag,
                int(math.floor(steps - (steps - 1) * math.log(count)
                / (math.log(max_count)or 1)))
            )
            for tag, count in tag_cloud_by_category[category]
        ]
        # put words in chaos
        random.shuffle(tag_cloud[category])
    sender.tag_cloud_by_category = tag_cloud

    sender._update_context(('tag_cloud_by_category', ))

def register():
    signals.article_generator_finalized.connect(tags_by_category)
