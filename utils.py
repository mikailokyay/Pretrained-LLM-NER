def unify_tags(output):
    all_entities_dict = {}
    unified_query = ""
    ex_tag = ""
    for idx, item in enumerate(output):
        tag = item['entity'].split("-")[1]
        if idx == 0:
            unified_query = item['word']
        elif ex_tag == tag and item['entity'].startswith("I"):
            unified_query = unified_query + " " + item['word']
        elif item['entity'].startswith("B"):
            all_entities_dict[unified_query] = ex_tag
            unified_query = item['word']

        ex_tag = tag

        if idx == len(output) - 1:
            all_entities_dict[unified_query] = ex_tag

    return all_entities_dict
