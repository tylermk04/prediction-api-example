library(plumber)
library(jsonlite)
library(glmnet)

model = readRDS("glm-1.Rds")

#* Echo the parameter that was sent in
#* @param msg The message to echo back.
#* @get /echo
function(msg=""){
  list(msg = paste0("The message is: '", msg, "'"))
}

#* Predict MPG
#* @post /predict
function (req) {
  json = jsonlite::fromJSON(req$postBody)
  cyl = json$cyl
  disp = json$disp
  hp = json$hp
  mpg = predict(model, rbind(c(cyl, disp, hp)), s=0.5)[1]
  list(mpg=mpg)
}
