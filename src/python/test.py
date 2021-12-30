import mlenv_cloud as mle

print(mle.__version__)

mle.create(docker_base_image="gcr.io/deeplearning-platform-release/tf-cpu",
           docker_image_bucket_name="news-ml-257304_cloudbuild")
