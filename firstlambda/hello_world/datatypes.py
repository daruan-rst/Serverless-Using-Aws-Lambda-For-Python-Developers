def simple_types(event, context):
    print(event)
    return event

def list_types(event, context):
    print(event)
    student_scores = {"john": 100, "bob": 90, "bharath": 100}
    scores = []
    for name in event:
        scores.append(student_scores[name])
    return scores

def dict_types(event, context):
    john_scores = event["john"]
    for score in john_scores:
        print(score)
    return event