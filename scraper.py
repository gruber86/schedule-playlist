from scrapy import Selector

source = 'source.htm'
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

def get_tracks(body, weekday):
    track_selector = '#{} .schedule__header .schedule__header--track'.format(weekday)
    tracks = body.css(track_selector)
    track_map = {}
    for track in tracks:
        track_name = track.xpath('text()').extract()[0].strip()
        track_id = track.css('div::attr(data-track)').extract()[0].strip()
        # print(track_name, track_id)
        track_map[track_id] = track_name
    return track_map


def get_events(body, weekday):
    event_selector = '#{} .schedule__body .event'.format(weekday)
    events = body.css(event_selector)
    for event in events:
        event_title = event.css('h3.name::text').extract()
        if not event_title:
            continue
        event_name = event_title[0].strip()
        print(event_name)


def main():
    body = Selector(text=open(source).read())
    events = []
    for day in weekdays:
        track_map = get_tracks(body, day)
        for track in sorted(track_map.items()):
            events.append(get_events(body, day))
        return events

if __name__ == '__main__':
    main()

