#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:29:41 2020

@author: ramonlopez
"""
"""All data is scrapped from Basketball Reference"""

#Import packages needed

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

""" Player Per Game Scraper function """

def player_pg(years):
    for i in years:
       # Get the corresponding url and parse it 
        years=years        
        url = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'.format(i)
        source = requests.get(url).text
        soup = BeautifulSoup(source,'lxml')
        
        #Get the header and rows into two separate list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
        headers = headers[1:]
        
        rows = soup.findAll('tr')[1:]
        player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
        
        #Creating the stats dataframe and getting rid of completely empty rows that were
        #included and replace remainding NaN values with 0. This is because of how Basketball Reference sets their tables up
        stats = pd.DataFrame(player_stats, columns = headers)
        stats = stats.replace('',np.nan)
        stats = stats.dropna(subset=['Player'])
        stats = stats.fillna(0)
        
        
        #Change the numerical columns from objects to floats and create a csv 
        float_col = [ 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P',
       '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',
       'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
        
        stats.insert(1,'Year',i)

        stats[float_col] = stats[float_col].astype(float)
        csv = '{}_players_pgs.csv'.format(i)
        stats.to_csv(csv,index=False)
        
    return


def player_tot(years):
    for i in years:
       # Get the corresponding url and parse it 
        years=years        
        url = 'https://www.basketball-reference.com/leagues/NBA_{}_totals.html'.format(i)
        source = requests.get(url).text
        soup = BeautifulSoup(source,'lxml')
        
        #Get the header and rows into two separate list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
        headers = headers[1:]
        
        rows = soup.findAll('tr')[1:]
        player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
        
        #Creating the stats dataframe and getting rid of completely empty rows that were
        #included and replace remainding NaN values with 0. This is because of how Basketball Reference sets their tables up
        stats = pd.DataFrame(player_stats, columns = headers)
        stats = stats.replace('',np.nan)
        stats = stats.dropna(subset=['Player'])
        stats = stats.fillna(0)
        
        
        #Change the numerical columns from objects to floats and create a csv 
        float_col = [ 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P',
       '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',
       'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
        
        stats.insert(1,'Year',i)

        stats[float_col] = stats[float_col].astype(float)
        csv = '{}_players_tot.csv'.format(i)
        stats.to_csv(csv,index=False)
        
    return
        
        
        
        
        
