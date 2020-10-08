import kfp
import kfp.dsl as dsl
from kfp import compiler
from kfp import components

EXPERIMENT_NAME = 'SIMPLE NOTEBOOK PIPELINE 2'
BASE_IMAGE = 'tensorflow/tensorflow:2.0.0b0-py3'


# Declare metadata for a pipeline
@dsl.pipeline(name='Calculation pipeline', description='A demo pipeline to show add operation')
# declare function and its return type
def add(a: float, b: float) -> float:
    import tensorflow as tf
    print('tf version', tf.__version__)
    print(a, '+', b, '=', a+b)
    return a+b


# Glue together 'add' function to the base_image.
add_op = components.func_to_container_op(add, base_image=BASE_IMAGE)


# make a new function to execute all the combinations of base add function
def calc_pipeline(a: float = 0, b: float = 7):
    add_task = add_op(a, 4)
    add_2_task = add_op(a, b)
    add_3_task = add_op(add_task.output, add_2_task.output)








# make a zip file of pipeline run
pipeline_func = calc_pipeline
pipeline_filename = pipeline_func.__name__ + '.pipeline.zip'
compiler.Compiler().compile(pipeline_func, pipeline_filename)

client = kfp.Client('http://10.152.183.83:3000')
experiment = client.create_experiment(EXPERIMENT_NAME)

arguments = {'a': '7', 'b': '8'}
run_name = pipeline_func.__name__ + 'run'
run_result = client.run_pipeline(experiment.id, run_name, pipeline_filename, arguments)
