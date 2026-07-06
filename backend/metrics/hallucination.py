from deepeval.metrics import HallucinationMetric


def create_metric(judge):

    return HallucinationMetric(
        model=judge,
        threshold=0.7
    )