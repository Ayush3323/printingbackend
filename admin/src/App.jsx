import { Routes, Route } from 'react-router-dom';
import MainLayout from './layouts/MainLayout';
import Dashboard from './pages/Dashboard';
import Reviews from './pages/Reviews';
import Customers from './pages/Customers';
import Products from './pages/Products';
import Categories from './pages/Categories';

function App() {
  return (
    <Routes>
      <Route path="/" element={<MainLayout />}>
        <Route index element={<Dashboard />} />
        <Route path="reviews" element={<Reviews />} />
        <Route path="customers" element={<Customers />} />
        <Route path="products" element={<Products />} />
        <Route path="categories" element={<Categories />} />
        <Route path="*" element={<div className="p-4">Page Not Found</div>} />
      </Route>
    </Routes>
  );
}

export default App;
