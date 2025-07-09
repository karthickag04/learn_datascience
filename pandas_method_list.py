"""
COMPREHENSIVE PANDAS METHODS REFERENCE
======================================
Complete list of pandas methods with brief explanations
Author: Reference Guide
"""

# =============================================================================
# PANDAS DATAFRAME METHODS
# =============================================================================

# DATA CREATION AND INPUT/OUTPUT
# DataFrame() - Create a DataFrame from various data sources
# read_csv() - Read CSV file into DataFrame
# read_excel() - Read Excel file into DataFrame
# read_json() - Read JSON file into DataFrame
# read_html() - Read HTML tables into DataFrame
# read_sql() - Read SQL query result into DataFrame
# read_parquet() - Read Parquet file into DataFrame
# read_pickle() - Read pickled pandas object
# read_feather() - Read Feather file into DataFrame
# read_hdf() - Read HDF5 file into DataFrame
# read_stata() - Read Stata file into DataFrame
# read_sas() - Read SAS file into DataFrame
# read_spss() - Read SPSS file into DataFrame
# read_clipboard() - Read data from clipboard
# read_fwf() - Read fixed-width formatted file
# read_table() - Read general delimited file
# read_xml() - Read XML file into DataFrame

# DATA OUTPUT
# to_csv() - Write DataFrame to CSV file
# to_excel() - Write DataFrame to Excel file
# to_json() - Write DataFrame to JSON file
# to_html() - Write DataFrame to HTML file
# to_sql() - Write DataFrame to SQL database
# to_parquet() - Write DataFrame to Parquet file
# to_pickle() - Write DataFrame to pickle file
# to_feather() - Write DataFrame to Feather file
# to_hdf() - Write DataFrame to HDF5 file
# to_stata() - Write DataFrame to Stata file
# to_clipboard() - Write DataFrame to clipboard
# to_string() - Convert DataFrame to string representation
# to_dict() - Convert DataFrame to dictionary
# to_records() - Convert DataFrame to structured array
# to_numpy() - Convert DataFrame to NumPy array
# to_latex() - Convert DataFrame to LaTeX table
# to_markdown() - Convert DataFrame to Markdown table
# to_xml() - Convert DataFrame to XML

# BASIC INFORMATION AND INSPECTION
# head() - Return first n rows
# tail() - Return last n rows
# info() - Print concise summary of DataFrame
# describe() - Generate descriptive statistics
# shape - Return tuple of (rows, columns)
# size - Return total number of elements
# ndim - Return number of dimensions
# dtypes - Return data types of columns
# columns - Return column labels
# index - Return row labels
# axes - Return list of axes
# empty - Return True if DataFrame is empty
# memory_usage() - Return memory usage of each column
# sample() - Return random sample of rows

# DATA SELECTION AND INDEXING
# loc[] - Access rows and columns by label
# iloc[] - Access rows and columns by integer position
# at[] - Access single scalar value by label
# iat[] - Access single scalar value by integer position
# get() - Get item from object for given key
# select_dtypes() - Select columns based on data type
# filter() - Filter DataFrame based on column/index names
# take() - Return elements at given indices
# query() - Query DataFrame using boolean expression
# where() - Replace values where condition is False
# mask() - Replace values where condition is True
# xs() - Return cross-section from hierarchical data

# COLUMN OPERATIONS
# drop() - Drop specified labels from rows or columns
# drop_duplicates() - Remove duplicate rows
# duplicated() - Return boolean Series denoting duplicate rows
# rename() - Rename columns or index
# rename_axis() - Set name of axis
# set_index() - Set DataFrame index using existing columns
# reset_index() - Reset index to default integer index
# reindex() - Reindex DataFrame to new index
# reindex_like() - Reindex to match another DataFrame
# assign() - Assign new columns to DataFrame
# insert() - Insert column into DataFrame at specified location
# pop() - Remove and return column

# ROW OPERATIONS
# append() - Append rows to end of DataFrame
# concat() - Concatenate DataFrames along axis
# join() - Join DataFrames using index
# merge() - Merge DataFrames using database-style joins
# transpose() - Transpose index and columns
# T - Property that returns transpose

# MISSING DATA HANDLING
# isnull() - Detect missing values
# isna() - Alias for isnull()
# notnull() - Detect non-missing values
# notna() - Alias for notnull()
# dropna() - Remove missing values
# fillna() - Fill missing values
# interpolate() - Interpolate missing values
# bfill() - Backward fill missing values
# ffill() - Forward fill missing values
# pad() - Alias for ffill()
# backfill() - Alias for bfill()

# SORTING AND RANKING
# sort_values() - Sort by values along axis
# sort_index() - Sort by index labels
# nlargest() - Return n largest values
# nsmallest() - Return n smallest values
# rank() - Compute numerical rank of values

# MATHEMATICAL OPERATIONS
# abs() - Return absolute values
# add() - Addition operation
# sub() - Subtraction operation
# mul() - Multiplication operation
# div() - Division operation
# truediv() - True division operation
# floordiv() - Floor division operation
# mod() - Modulo operation
# pow() - Exponential power operation
# round() - Round values to specified decimals
# clip() - Limit values to specified range
# cumsum() - Cumulative sum
# cumprod() - Cumulative product
# cummax() - Cumulative maximum
# cummin() - Cumulative minimum
# diff() - Calculate difference between consecutive elements
# pct_change() - Percentage change between elements

# STATISTICAL OPERATIONS
# count() - Count non-null values
# sum() - Sum of values
# mean() - Mean of values
# median() - Median of values
# mode() - Mode of values
# std() - Standard deviation
# var() - Variance
# min() - Minimum value
# max() - Maximum value
# quantile() - Return quantile values
# skew() - Return skewness
# kurt() - Return kurtosis
# sem() - Return standard error of mean
# mad() - Return mean absolute deviation
# prod() - Return product of values
# nunique() - Count unique values
# value_counts() - Count unique values with frequencies
# corr() - Compute correlation matrix
# cov() - Compute covariance matrix

# GROUPING AND AGGREGATION
# groupby() - Group DataFrame using mapper or column names
# agg() - Aggregate using specified functions
# aggregate() - Alias for agg()
# apply() - Apply function along axis
# transform() - Transform data using function
# pipe() - Apply function to DataFrame
# rolling() - Provide rolling window calculations
# expanding() - Provide expanding window calculations
# ewm() - Provide exponentially weighted calculations
# resample() - Resample time-series data

# STRING OPERATIONS (for object columns)
# str.contains() - Test if pattern is contained in string
# str.startswith() - Test if string starts with pattern
# str.endswith() - Test if string ends with pattern
# str.upper() - Convert strings to uppercase
# str.lower() - Convert strings to lowercase
# str.title() - Convert strings to title case
# str.capitalize() - Capitalize first letter
# str.strip() - Remove leading/trailing whitespace
# str.replace() - Replace substring in string
# str.split() - Split strings by delimiter
# str.extract() - Extract groups from string using regex
# str.len() - Return string length
# str.slice() - Slice strings
# str.cat() - Concatenate strings
# str.count() - Count substring occurrences
# str.find() - Find substring position
# str.isdigit() - Check if string contains only digits
# str.isalpha() - Check if string contains only letters
# str.isalnum() - Check if string is alphanumeric

# DATETIME OPERATIONS
# dt.date - Extract date component
# dt.time - Extract time component
# dt.year - Extract year
# dt.month - Extract month
# dt.day - Extract day
# dt.hour - Extract hour
# dt.minute - Extract minute
# dt.second - Extract second
# dt.dayofweek - Extract day of week
# dt.dayofyear - Extract day of year
# dt.weekday - Extract weekday
# dt.quarter - Extract quarter
# dt.strftime() - Format datetime as string
# dt.normalize() - Normalize to midnight
# dt.tz_localize() - Localize timezone
# dt.tz_convert() - Convert timezone

# DATA TYPE CONVERSION
# astype() - Cast to specified data type
# convert_dtypes() - Convert to best possible dtypes
# infer_objects() - Infer better dtypes for object columns
# to_numeric() - Convert to numeric type
# to_datetime() - Convert to datetime type
# to_timedelta() - Convert to timedelta type

# ITERATION
# items() - Iterate over column names and series
# iterrows() - Iterate over rows as (index, Series) pairs
# itertuples() - Iterate over rows as named tuples
# keys() - Get column names

# RESHAPING AND PIVOTING
# pivot() - Reshape data based on column values
# pivot_table() - Create spreadsheet-style pivot table
# melt() - Unpivot DataFrame from wide to long format
# wide_to_long() - Wide panel to long format
# stack() - Stack prescribed level(s) from columns to index
# unstack() - Unstack prescribed level(s) from index to columns
# explode() - Transform list-like elements to individual rows

# BOOLEAN OPERATIONS
# all() - Return True if all values are True
# any() - Return True if any value is True
# equals() - Test whether two objects contain same elements
# isin() - Check if values are contained in given list

# COMPARISON OPERATIONS
# eq() - Element-wise equality comparison
# ne() - Element-wise not equal comparison
# lt() - Element-wise less than comparison
# le() - Element-wise less than or equal comparison
# gt() - Element-wise greater than comparison
# ge() - Element-wise greater than or equal comparison
# between() - Check if values are between bounds

# PLOTTING (requires matplotlib)
# plot() - Create various types of plots
# hist() - Create histogram
# boxplot() - Create box plot
# scatter() - Create scatter plot

# ADVANCED OPERATIONS
# eval() - Evaluate string expression
# combine() - Combine DataFrame with another using function
# combine_first() - Combine with another DataFrame, filling missing values
# update() - Modify DataFrame in place using values from another DataFrame
# align() - Align DataFrames on their indices
# lookup() - Label-based fancy indexing function
# set_flags() - Return new object with flags set

# =============================================================================
# PANDAS SERIES METHODS
# =============================================================================

# SERIES CREATION
# Series() - Create a Series from various data sources

# BASIC PROPERTIES
# name - Name of the Series
# dtype - Data type of Series
# hasnans - Return True if Series has any NaN values
# is_monotonic - Return True if values are monotonic
# is_monotonic_increasing - Return True if values are monotonic increasing
# is_monotonic_decreasing - Return True if values are monotonic decreasing
# is_unique - Return True if values are unique
# nbytes - Return number of bytes

# INDEXING AND SELECTION
# get() - Get value for given key
# item() - Return first element of underlying data as scalar
# keys() - Alias for index
# pop() - Remove and return item at index
# take() - Return elements at given positions
# truncate() - Truncate Series before and after given indices

# MATHEMATICAL OPERATIONS (similar to DataFrame)
# All arithmetic operations available for DataFrame

# STATISTICAL OPERATIONS (similar to DataFrame)
# All statistical operations available for DataFrame

# STRING OPERATIONS (when dtype is object)
# All string operations available for DataFrame

# DATETIME OPERATIONS (when dtype is datetime)
# All datetime operations available for DataFrame

# CATEGORICAL OPERATIONS (when dtype is category)
# cat.categories - Get categories
# cat.ordered - Check if categorical is ordered
# cat.codes - Get category codes
# cat.add_categories() - Add new categories
# cat.remove_categories() - Remove categories
# cat.rename_categories() - Rename categories
# cat.reorder_categories() - Reorder categories
# cat.remove_unused_categories() - Remove unused categories
# cat.set_categories() - Set categories

# SPARSE OPERATIONS (when dtype is sparse)
# sparse.density - Get density of sparse Series
# sparse.fill_value - Get fill value for sparse Series
# sparse.npoints - Get number of non-fill-value points
# sparse.to_dense() - Convert sparse to dense Series

# UNIQUE AND DUPLICATES
# unique() - Return unique values
# nunique() - Count unique values
# is_unique - Check if values are unique
# drop_duplicates() - Remove duplicate values
# duplicated() - Mark duplicate values

# CONVERSION
# to_list() - Convert to Python list
# tolist() - Alias for to_list()
# to_frame() - Convert Series to DataFrame

# =============================================================================
# PANDAS INDEX METHODS
# =============================================================================

# INDEX CREATION
# Index() - Create basic Index
# RangeIndex() - Create range-based Index
# Int64Index() - Create integer Index
# Float64Index() - Create float Index
# DatetimeIndex() - Create datetime Index
# TimedeltaIndex() - Create timedelta Index
# PeriodIndex() - Create period Index
# CategoricalIndex() - Create categorical Index
# MultiIndex() - Create hierarchical Index
# IntervalIndex() - Create interval Index

# INDEX PROPERTIES
# name - Name of the Index
# names - Names of levels in MultiIndex
# nlevels - Number of levels in Index
# is_monotonic - Check if Index is monotonic
# is_monotonic_increasing - Check if Index is monotonic increasing
# is_monotonic_decreasing - Check if Index is monotonic decreasing
# is_unique - Check if Index values are unique
# has_duplicates - Check if Index has duplicate values

# INDEX OPERATIONS
# append() - Append another Index
# delete() - Delete item at given position
# drop() - Drop given labels
# drop_duplicates() - Remove duplicate values
# insert() - Insert item at given position
# union() - Compute union of Indexes
# intersection() - Compute intersection of Indexes
# difference() - Compute difference of Indexes
# symmetric_difference() - Compute symmetric difference
# join() - Join Indexes
# sort_values() - Sort Index values
# argsort() - Get integer indices for sorting
# searchsorted() - Find insertion points for values
# get_level_values() - Get values for given level in MultiIndex
# droplevel() - Remove level from MultiIndex
# swaplevel() - Swap levels in MultiIndex

# =============================================================================
# PANDAS GENERAL FUNCTIONS
# =============================================================================

# UTILITY FUNCTIONS
# concat() - Concatenate pandas objects
# merge() - Merge DataFrames using database-style joins
# merge_asof() - Perform asof merge
# merge_ordered() - Merge with optional filling/interpolation
# crosstab() - Compute cross-tabulation
# cut() - Bin values into discrete intervals
# qcut() - Bin values into equal-sized buckets
# get_dummies() - Convert categorical variables to dummy variables
# factorize() - Encode input values as enumerated type
# unique() - Return unique values from array-like
# value_counts() - Count unique values
# lreshape() - Reshape wide-format data to long
# wide_to_long() - Wide panel to long format

# TIME SERIES FUNCTIONS
# date_range() - Generate range of dates
# bdate_range() - Generate range of business dates
# period_range() - Generate range of periods
# timedelta_range() - Generate range of timedeltas
# infer_freq() - Infer frequency of datetime index
# to_datetime() - Convert to datetime
# to_timedelta() - Convert to timedelta
# to_numeric() - Convert to numeric

# OPTION FUNCTIONS
# set_option() - Set pandas option
# get_option() - Get pandas option
# reset_option() - Reset pandas option
# describe_option() - Describe pandas option
# option_context() - Context manager for options

# TESTING FUNCTIONS
# testing.assert_frame_equal() - Check DataFrame equality
# testing.assert_series_equal() - Check Series equality
# testing.assert_index_equal() - Check Index equality

# API FUNCTIONS
# api.types.is_datetime64_any_dtype() - Check if dtype is datetime-like
# api.types.is_numeric_dtype() - Check if dtype is numeric
# api.types.is_object_dtype() - Check if dtype is object
# api.types.is_categorical_dtype() - Check if dtype is categorical
# api.types.is_string_dtype() - Check if dtype is string
# api.types.is_integer_dtype() - Check if dtype is integer
# api.types.is_float_dtype() - Check if dtype is float
# api.types.is_bool_dtype() - Check if dtype is boolean

# =============================================================================
# PANDAS PLOTTING METHODS (requires matplotlib)
# =============================================================================

# DATAFRAME PLOTTING
# plot.line() - Line plot
# plot.bar() - Bar plot
# plot.barh() - Horizontal bar plot
# plot.hist() - Histogram
# plot.box() - Box plot
# plot.kde() - Kernel density estimation plot
# plot.density() - Alias for kde()
# plot.area() - Area plot
# plot.pie() - Pie chart
# plot.scatter() - Scatter plot
# plot.hexbin() - Hexagonal bin plot

# SERIES PLOTTING
# All DataFrame plotting methods available for Series

print("📚 PANDAS METHODS REFERENCE GUIDE LOADED")
print("💡 This file contains comprehensive list of pandas methods")
print("🔍 Use Ctrl+F to search for specific methods")
print("📖 Each method includes brief explanation in comments")