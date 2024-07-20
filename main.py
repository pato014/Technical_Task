import requests


# get data
def get_data(url: str) -> list:
    data = requests.get(url).json()
    return data


# get 3 highest scores
def get_max_three(data):
    count = 0
    names_with_scores = []
    while count < 3:
        item_with_max_score = max(data, key=lambda x: x.get('score'))
        names_with_scores.append(f"{item_with_max_score.get('name')}:{item_with_max_score.get('score')}")
        data.remove(item_with_max_score)
        count += 1

    return names_with_scores


def task_1(url: str) -> list:
    data = get_data(url)
    return get_max_three(data)


def task_2(url: str) -> list:
    data = get_data(url)
    all_items = []
    for elem in data:
        all_items.append({"name": elem.get('name'), "score": elem.get('score')})
        child_elem = elem.get('children')
        for child in child_elem:
            all_items.append({"name": child.get('name'), "score": child.get('score')})

    return get_max_three(all_items)


def task_3(url: str) -> list:
    data = get_data(url)
    scores = []

    def recurse(node):
        scores.append({"name": node['name'], "score": node['score']})
        for child in node.get("children"):
            if len(node.get("children")) > 0:
                recurse(child)

    for entry in data:
        recurse(entry)

    return get_max_three(scores)


print(f'task 1: {task_1("https://geoavia.com/tasks/algorithm/1.json")}')
print(f'task 2: {task_2("https://geoavia.com/tasks/algorithm/2.json")}')
print(f'task 3: {task_3("https://geoavia.com/tasks/algorithm/3.json")}')
