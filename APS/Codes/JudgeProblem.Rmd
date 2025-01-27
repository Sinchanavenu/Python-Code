---
title: "Intro to R"
output:
  pdf_document: default
  html_document:
    df_print: paged
editor_options:
  chunk_output_type: console
---

#### Execute the following cells to load the libraries
```{r}
library(ggplot2)
library(dplyr)
```

#### Creating homeogenous datastructures: vectors and matrices (built on the fundamental datatypes character, numeric, integer, and logical)
```{r}
myvector1 = c(1,2,3)
myvector2 = c('a', 'b', 'c')
myvector3 = c(TRUE, FALSE, FALSE)
myvector4 = c(1.5, 4.5, 2.3)
myvector5 = 1:10
myvector6 = seq(1,10, by=0.5)

print(myvector1)
print(myvector2)
print(myvector3)
print(myvector4)
print(myvector5)
print(myvector6)

mymatrix1 = matrix(c(1,2,3,4,5,6), nrow=2, ncol=3)

print(mymatrix1)
```

#### Creating a list, a heterogenous datastructure
```{r}
mylist = list(1, 'Name', c('ALA', 'APS', 'DL'))
print(mylist)
```

#### Accessing elements of a datastructure
```{r}
myvector1[1]
myvector6[10]
mymatrix1[1,2]
mymatrix1[1,]
mymatrix1[,2]
```

#### Loading data into a dataframe, a heterogenous datastructure
```{r}
#file = 'http://openmv.net/file/food-texture.csv'
file = 'Data/food-texture.csv'
foodData = read.csv(file, header = TRUE, row.names = 1, stringsAsFactors = FALSE)
head(foodData, 5)
```

#### Attributes of a dataframe
```{r}
str(foodData)
nrow(foodData)
ncol((foodData))
colnames(foodData)
rownames(foodData)
```

#### Get the data type and the data structure associated with an object
```{r}
myvector1
typeof(myvector1)
```

#### Accessing elements of a data frame
```{r}
foodData$Oil
foodData[['Oil']]
foodData[1,'Oil']
foodData['B110', 'Oil']
```

#### Accessing elements of a particular column of a data frame
```{r}
foodData[1,'Oil']
```

#### Accessing elements of multiple columns of a dataframe (using base R and dplyr)
```{r}
foodData[c('Oil','Density')]
foodData %>% select(c(Oil, Density))
```

#### Matrix example - judges problem
```{r}

courtdecision = function(){
  jcp = c(0.95, 0.95, 0.90, 0.90, 0.80)
  jicp = 1-jcp # broadcasting
  p = matrix(c(jcp, jicp), nrow=2, ncol=5, byrow=TRUE)
  decision = c(1, 0)
  cdecision = vector('integer', ncol(p))
  for (j in 1:ncol(p)){
    cdecision[j] = sample(decision, 1, replace=FALSE, prob=c(jcp[j], jicp[j]))
  }
  if (sum(cdecision) >= 3){
    return(0)
    }
  else{
    return(1)
}
}
courtdecision()
```

#### Court incorrect probability
```{r}
results = replicate(1000, courtdecision())
print(mean(results))
```

#### Accessing rows of a dataframe satisfying certain conditions
```{r}
```

#### Accessing row of a dataframe satisfying certain condition and particular columns
```{r}
```

#### Accessing rows of a dataframe satisfying certain conditions
```{r}
#Filter samples with Crispy index 9 or 15 (which are very rare)
```

#### Modifying a column of a dataframe
```{r}
```

#### Modify Crispy column to reflect high (0) or low (1) crispiness
```{r}
```

##### Change Crispy and Crispylevel columns to factor (categorical) type
```{r}
categorical_cols = c('Crispy', 'Crispylevel')
foodData[categorical_cols] = lapply(?, ?)
str(foodData)
```

#### Visualize the OilPercentage feature
```{r}
```

#### In-built functions for dataframes
```{r}
# Mean oil percentage across all samples

# Mean-centering of OilPercentage

# Sum of the squared deviation from the mean

# Average of the squared deviation from the mean

# Variance of OilPercentage

# Standard deviation of OilPercentage
```

#### Scatter plot between OilPercentage and Density
```{r}
```

#### Scatter plot between OilPercentage and Density color coded with Crispylevel
```{r}
```

#### Scale continuous columns of the dataframe
```{r}
```

#### Calculate the correlation matrix for the continuous features
```{r}

```

#### Scatter plot between Density and Hardness
```{r}
```

#### Scatter plot between Density and Fracture
```{r}
```













