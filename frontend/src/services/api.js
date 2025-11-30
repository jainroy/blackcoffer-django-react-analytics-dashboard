import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';
const api = axios.create({ baseURL: API_BASE_URL });

export const fetchEntries = (filters = {}) => {
  const params = new URLSearchParams();
  if (filters.topic) params.append('topic', filters.topic);
  if (filters.region) params.append('region', filters.region);
  params.append('page', filters.page || 1);
  params.append('page_size', filters.pageSize || 10);
  return api.get('/entries/', { params });
};

export const fetchFilters = () => api.get('/filters/');

// FIXED: Use year field instead of published date
export const fetchIntensityByYear = () => api.get('/aggregations/intensity-by-year/');
export const fetchLikelihoodTrend = () => api.get('/aggregations/likelihood-trend/');