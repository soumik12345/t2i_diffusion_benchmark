from t2i_diffusion_benchmark.metrics import (
    CLIPImageQualityScorer,
    CLIPScorer,
    BLIPScorer,
)
from t2i_diffusion_benchmark.eval_pipelines import StableDiffusionEvaluationPipeline


if __name__ == "__main__":
    dataset = [
        {"prompt": "a photo of an astronaut riding a horse on mars"},
        {"prompt": "A high tech solarpunk utopia in the Amazon rainforest"},
        # {"prompt": "A pikachu fine dining with a view to the Eiffel Tower"},
        # {"prompt": "A mecha robot in a favela in expressionist style"},
        # {"prompt": "an insect robot preparing a delicious meal"},
        # {
        #     "prompt": "A small cabin on top of a snowy mountain in the style of Disney, artstation"
        # },
    ]

    diffuion_evaluation_pipeline = StableDiffusionEvaluationPipeline(
        "CompVis/stable-diffusion-v1-4"
    )

    # # Add CLIP Scorer metric
    # clip_scorer = CLIPScorer()
    # diffuion_evaluation_pipeline.add_metric(clip_scorer)

    # # Add CLIP IQA Metric
    # clip_iqa_scorer = CLIPImageQualityScorer()
    # diffuion_evaluation_pipeline.add_metric(clip_iqa_scorer)

    blip_scorer = BLIPScorer()
    diffuion_evaluation_pipeline.add_metric(blip_scorer)

    diffuion_evaluation_pipeline(
        dataset=dataset, init_params=dict(project="t2i_eval", entity="geekyrakshit")
    )
