from deepeval.metrics import AnswerRelevancyMetric


def create_metric(judge):

    return AnswerRelevancyMetric(
        model=judge,
        threshold=0.7
    )