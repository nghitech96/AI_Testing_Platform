from backend.metrics.answer_relevancy import create_metric as answer_relevancy
from backend.metrics.hallucination import create_metric as hallucination
from backend.metrics.bias import create_metric as bias
from backend.metrics.toxicity import create_metric as toxicity


class MetricFactory:

    METRICS = {
        "answer_relevancy": answer_relevancy,
        "hallucination": hallucination,
        "bias": bias,
        "toxicity": toxicity,
    }

    @classmethod
    def create(cls, metric_name, judge):

        metric_name = metric_name.lower()

        if metric_name not in cls.METRICS:
            raise ValueError(
                f"Unsupported metric: {metric_name}"
            )

        return cls.METRICS[metric_name](judge)