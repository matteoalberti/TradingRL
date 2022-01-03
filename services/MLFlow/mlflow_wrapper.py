import mlflow


class mlflow_wrapper():
    def __init__(self, tags):
        self.project = tags.get("project")
        self.agent = tags.get("agent")

    # TODO : add figures

    def mlflow_base(self, hyperparams):
        with mlflow.start_run(nested=True):
            t = {"project" : self.project}
            mlflow.set_tag(t)

    def mlflow_tensorflow(self, hyperparams):
        mlflow.tensorflow.autolog()
        with mlflow.start_run(nested=True):
            t = {"project" : self.project}
            mlflow.set_tag(t)
            #Compiled model, to be fitted

            #Evaluate

    def mlflow_sklearn(self, hyperparams):
        mlflow.sklearn.autolog()
        with mlflow.start_run(nested=True):
            t = {"project" : self.project, "agent" : self.agent}
            mlflow.set_tag(t)
            #compiled model, to be fitted

            #Evaluate

    def mlflow_rl(self, hyperparams, invest, total_gains, im):
        mlflow.tensorflow.autolog()
        with mlflow.start_run(nested=True):
            t = {"project" : self.project, "agent" : self.agent}
            p = {"initial_money" : hyperparams.get("initial_money"),"max_buy":hyperparams.get("max_buy"),
                                                         "max_sell":hyperparams.get("max_sell")}
            m = {"invest":invest, "total_gains" : total_gains}

            mlflow.set_tags(t)
            mlflow.log_params(p)
            mlflow.log_metrics(m)

            mlflow.log_image(im, "{}_eur_usd.png".format(self.project))