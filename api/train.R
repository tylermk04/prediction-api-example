library(glmnet)

x = as.matrix(mtcars[,c(2, 3, 4)])
y = lapply(mtcars[1], as.numeric)[1]$mpg

model = glmnet(x, y)

res = predict(model, rbind(c(8, 200, 245)), s=4)[1]

res + 1

saveRDS(model, 'glm-1.Rds')
