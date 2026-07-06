from deepeval.metrics import BiasMetric


def create_metric(judge):

    return BiasMetric(
        model=judge,
        threshold=0.7
    )