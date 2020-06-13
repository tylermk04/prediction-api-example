library(plumber)

p = plumber::plumb("api.R")
p$run()
