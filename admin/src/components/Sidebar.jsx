import React from 'react';
import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  ShoppingCart,
  Package,
  Users,
  CreditCard,
  Megaphone,
  Tag,
  Image,
  Box,
  Truck,
  BarChart2,
  Settings
} from 'lucide-react';
import './Sidebar.css';

const Sidebar = () => {
  const menuItems = [
    { icon: LayoutDashboard, label: 'Dashboard', path: '/' },
    { icon: ShoppingCart, label: 'Orders', path: '/orders' },
    { icon: Package, label: 'Products', path: '/products' },
    { icon: Tag, label: 'Categories', path: '/categories' },
    { icon: Users, label: 'Customers', path: '/customers' },
    { icon: CreditCard, label: 'Payments', path: '/payments' },
    { icon: Megaphone, label: 'Marketing', path: '/marketing' },
    { icon: Image, label: 'Navbar Images', path: '/navbar-images' },
    { icon: Box, label: 'Stocks', path: '/stocks' },
    { icon: Truck, label: 'Courier', path: '/courier' },
    { icon: BarChart2, label: 'Finance', path: '/finance' },
    { icon: Settings, label: 'Managment', path: '/reviews' }, // Mapping 'Managment' to Reviews based on request or just as a placeholder, actually user asked for Reviews page, I'll map Management to Reviews for now or add a separate Reviews item. 
    // Wait, the image shows "Managment" at bottom. The user asked for "Reviews View Implementation".
    // I will add "Reviews" explicitly if it's not "Managment". Let's assume one of these is the entry point or I'll just add it.
    // Actually, let's Stick to the image for the sidebar but route 'Managment' to the reviews page for this demo, or add a specific Reviews link?
    // Let's route 'Managment' to '/reviews' as the user wants to see the Reviews page.
  ];

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <h2 className="admin-title">ADMIN DASHBOARD</h2>
      </div>
      <nav className="sidebar-nav">
        {menuItems.map((item) => (
          <NavLink
            key={item.label}
            to={item.path}
            className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
          >
            <item.icon size={20} className="nav-icon" />
            <span className="nav-label">{item.label}</span>
          </NavLink>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;
