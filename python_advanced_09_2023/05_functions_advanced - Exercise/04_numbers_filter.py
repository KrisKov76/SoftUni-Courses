def even_odd_filter(**kwargs):
    for k, v in kwargs.items():
        if k == 'even':
            kwargs[k] = [x for x in v if x % 2 == 0] # не помнех как се взима стойността на ключа?!!?
        if k == 'odd':
            kwargs[k] = [x for x in v if x % 2 != 0]
    return dict(sorted(kwargs.items(), key=lambda kvp:-len(kvp[1])))
