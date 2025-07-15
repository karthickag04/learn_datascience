"""
Karthickag - Custom Pandas-like module for data operations
Author: Karthick
"""

import pandas as pd
import os
import numpy as np

class DataReader:
    """Custom data reading class with pandas-like methods"""
    
    def __init__(self, base_path="data"):
        self.base_path = base_path
        
    def read_csv(self, filename, **kwargs):
        """
        Read CSV file using pandas
        
        Args:
            filename (str): Name of the CSV file
            **kwargs: Additional arguments for pd.read_csv()
            
        Returns:
            pandas.DataFrame: Loaded dataframe
        """
        file_path = os.path.join(self.base_path, filename)
        try:
            df = pd.read_csv(file_path, **kwargs)
            print(f"✓ Successfully loaded {filename}")
            print(f"  Shape: {df.shape}")
            return df
        except FileNotFoundError:
            print(f"✗ File {filename} not found in {self.base_path}")
            return None
        except Exception as e:
            print(f"✗ Error loading {filename}: {str(e)}")
            return None
    
    def read_excel(self, filename, **kwargs):
        """
        Read Excel file using pandas
        
        Args:
            filename (str): Name of the Excel file
            **kwargs: Additional arguments for pd.read_excel()
            
        Returns:
            pandas.DataFrame: Loaded dataframe
        """
        file_path = os.path.join(self.base_path, filename)
        try:
            df = pd.read_excel(file_path, **kwargs)
            print(f"✓ Successfully loaded {filename}")
            print(f"  Shape: {df.shape}")
            return df
        except FileNotFoundError:
            print(f"✗ File {filename} not found in {self.base_path}")
            return None
        except Exception as e:
            print(f"✗ Error loading {filename}: {str(e)}")
            return None

class DataAnalyzer:
    """Custom data analysis class with pandas-like methods"""
    
    @staticmethod
    def quick_info(df, name="Dataset"):
        """
        Display quick information about the dataframe
        
        Args:
            df (pandas.DataFrame): Input dataframe
            name (str): Name of the dataset for display
        """
        print(f"\n{'='*50}")
        print(f"{name.upper()} OVERVIEW")
        print(f"{'='*50}")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print(f"Data Types:\n{df.dtypes}")
        print(f"\nMemory Usage: {df.memory_usage().sum() / 1024**2:.2f} MB")
        
    @staticmethod
    def missing_values_report(df):
        """
        Generate missing values report
        
        Args:
            df (pandas.DataFrame): Input dataframe
            
        Returns:
            pandas.DataFrame: Missing values report
        """
        missing = df.isnull().sum()
        missing_percent = (missing / len(df)) * 100
        
        missing_df = pd.DataFrame({
            'Column': missing.index,
            'Missing_Count': missing.values,
            'Missing_Percentage': missing_percent.values
        })
        
        missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)
        
        if len(missing_df) > 0:
            print("\n📊 MISSING VALUES REPORT:")
            print(missing_df.to_string(index=False))
        else:
            print("\n✓ No missing values found!")
            
        return missing_df
    
    @staticmethod
    def data_summary(df):
        """
        Generate comprehensive data summary
        
        Args:
            df (pandas.DataFrame): Input dataframe
        """
        print("\n📈 STATISTICAL SUMMARY:")
        print(df.describe(include='all'))
        
        print("\n🔢 NUMERICAL COLUMNS:")
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        print(f"Count: {len(numeric_cols)}")
        print(f"Columns: {numeric_cols}")
        
        print("\n📝 CATEGORICAL COLUMNS:")
        cat_cols = df.select_dtypes(include=['object']).columns.tolist()
        print(f"Count: {len(cat_cols)}")
        print(f"Columns: {cat_cols}")
        
    @staticmethod
    def head(df, n=5):
        """
        Display first n rows of dataframe
        
        Args:
            df (pandas.DataFrame): Input dataframe
            n (int): Number of rows to display
            
        Returns:
            pandas.DataFrame: First n rows
        """
        print(f"\n📋 FIRST {n} ROWS:")
        result = df.head(n)
        print(result)
        return result
    
    @staticmethod
    def tail(df, n=5):
        """
        Display last n rows of dataframe
        
        Args:
            df (pandas.DataFrame): Input dataframe
            n (int): Number of rows to display
            
        Returns:
            pandas.DataFrame: Last n rows
        """
        print(f"\n📋 LAST {n} ROWS:")
        result = df.tail(n)
        print(result)
        return result

class DataCleaner:
    """Custom data cleaning class with pandas-like methods"""
    
    @staticmethod
    def drop_missing(df, threshold=0.5):
        """
        Drop columns with missing values above threshold
        
        Args:
            df (pandas.DataFrame): Input dataframe
            threshold (float): Threshold for missing values (0.5 = 50%)
            
        Returns:
            pandas.DataFrame: Cleaned dataframe
        """
        missing_percent = df.isnull().sum() / len(df)
        cols_to_drop = missing_percent[missing_percent > threshold].index.tolist()
        
        if cols_to_drop:
            print(f"🗑️ Dropping columns with >{threshold*100}% missing values:")
            print(f"  Columns: {cols_to_drop}")
            return df.drop(columns=cols_to_drop)
        else:
            print(f"✓ No columns with >{threshold*100}% missing values found")
            return df.copy()
    
    @staticmethod
    def fill_missing(df, strategy='mean'):
        """
        Fill missing values with specified strategy
        
        Args:
            df (pandas.DataFrame): Input dataframe
            strategy (str): 'mean', 'median', 'mode', or 'forward_fill'
            
        Returns:
            pandas.DataFrame: Dataframe with filled missing values
        """
        df_filled = df.copy()
        
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                if df[col].dtype in ['int64', 'float64']:
                    if strategy == 'mean':
                        df_filled[col] = df_filled[col].fillna(df[col].mean())
                    elif strategy == 'median':
                        df_filled[col] = df_filled[col].fillna(df[col].median())
                elif df[col].dtype == 'object':
                    if strategy == 'mode':
                        df_filled[col] = df_filled[col].fillna(df[col].mode()[0])
                
                if strategy == 'forward_fill':
                    df_filled[col] = df_filled[col].fillna(method='ffill')
        
        print(f"✓ Missing values filled using {strategy} strategy")
        return df_filled

# Create instances for easy importing
reader = DataReader()
analyzer = DataAnalyzer()
cleaner = DataCleaner()

# Convenience functions (pandas-like interface)
def read_csv(filename, **kwargs):
    """Convenience function to read CSV"""
    return reader.read_csv(filename, **kwargs)

def read_excel(filename, **kwargs):
    """Convenience function to read Excel"""
    return reader.read_excel(filename, **kwargs)

def info(df, name="Dataset"):
    """Convenience function for quick info"""
    return analyzer.quick_info(df, name)

def head(df, n=5):
    """Convenience function for head"""
    return analyzer.head(df, n)

def tail(df, n=5):
    """Convenience function for tail"""
    return analyzer.tail(df, n)

def missing_report(df):
    """Convenience function for missing values report"""
    return analyzer.missing_values_report(df)

def summary(df):
    """Convenience function for data summary"""
    return analyzer.data_summary(df)