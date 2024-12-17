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