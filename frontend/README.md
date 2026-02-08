# React Frontend - Facts Display App

## 📌 Overview
This React application fetches and displays interesting facts from a Django REST API backend.

## 🚀 Tech Stack
- **React** 19.2.4
- **JavaScript** (ES6+)
- **CSS3** (Custom styling, no frameworks)
- **Fetch API** (for HTTP requests)

## 📂 Project Structure

```
frontend/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── App.js          # Main component with API integration
│   ├── App.css         # Component styling
│   ├── index.js        # React entry point
│   └── index.css       # Global styles
├── package.json
└── README.md
```

## 🔧 How It Works

### App.js Explained

1. **React Hooks Used:**
   - `useState` - Manages facts data, loading state, and errors
   - `useEffect` - Fetches data from API when component mounts

2. **API Integration:**
   ```javascript
   const API_URL = 'http://127.0.0.1:8000/api/facts/';
   ```

3. **Data Flow:**
   - Component mounts → `useEffect` runs
   - Fetch data from Django API
   - Update state with fetched facts
   - Render facts in UI

4. **States:**
   - **Loading**: Shows spinner while fetching
   - **Error**: Shows error message if API fails
   - **Success**: Displays facts in cards

## 💻 Running the Application

### Prerequisites
- Node.js installed
- Django backend running on `http://127.0.0.1:8000`

### Installation & Start

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies (first time only)
npm install

# Start development server
npm start
```

The app will open automatically in your browser at:
- **http://localhost:3001** (or 3000 if available)

## 🎨 Features

### ✅ Implemented Features
1. **API Integration** - Fetches data from Django REST API
2. **Loading State** - Animated spinner while loading
3. **Error Handling** - User-friendly error messages
4. **Responsive Design** - Works on mobile, tablet, desktop
5. **Card Layout** - Each fact in a beautiful card
6. **Hover Effects** - Interactive UI elements
7. **Category Tags** - Facts organized by category

### 🎯 Key Components

#### Fact Card
Each fact displays:
- **ID number** - Unique identifier
- **Category badge** - Color-coded category
- **Fact text** - The actual interesting fact

## 🌐 API Integration Details

### Endpoint Used
```
GET http://127.0.0.1:8000/api/facts/
```

### Expected Response Format
```json
{
  "success": true,
  "count": 10,
  "message": "Facts retrieved successfully",
  "data": [
    {
      "id": 1,
      "fact": "Python was named after Monty Python...",
      "category": "Programming"
    }
  ]
}
```

### Error Handling
The app handles:
- Network errors
- HTTP errors (404, 500, etc.)
- JSON parsing errors
- Backend not running

## 🎨 Styling

### Design Choices
- **Purple Gradient Background** - Modern, professional look
- **White Cards** - Clean, readable content
- **Hover Effects** - Interactive feedback
- **Responsive Grid** - Adapts to screen size

### CSS Features
- Flexbox & Grid layouts
- CSS animations (spinner, hover)
- Media queries for responsiveness
- Custom color scheme

## 📱 Responsive Breakpoints

```css
Desktop: > 768px    (Multi-column grid)
Tablet:  768px     (Responsive grid)
Mobile:  < 480px   (Single column)
```

## 🔍 Troubleshooting

### Common Issues

#### 1. "Failed to fetch" Error
**Problem**: Backend not running
**Solution**: Start Django server
```bash
cd backend
python manage.py runserver
```

#### 2. CORS Error
**Problem**: CORS not configured
**Solution**: Check Django `settings.py` has correct CORS origins

#### 3. Blank Page
**Problem**: JavaScript error
**Solution**: Check browser console (F12) for errors

#### 4. Port Already in Use
**Problem**: Port 3000/3001 occupied
**Solution**: React will prompt to use another port, type 'Y'

## 📦 Available Scripts

```bash
# Start development server
npm start

# Create production build
npm run build

# Run tests
npm test

# Eject configuration (⚠️ irreversible)
npm eject
```

## 🚀 Production Build

To create an optimized production build:

```bash
npm run build
```

This creates a `build/` folder with optimized static files ready for deployment.

## 📚 Learning Points

### Key Concepts Covered
1. **React Hooks** (useState, useEffect)
2. **Fetch API** for HTTP requests
3. **Async/Await** for handling promises
4. **Component State Management**
5. **Conditional Rendering**
6. **CSS Grid & Flexbox**
7. **Responsive Web Design**
8. **Error Handling in React**

## 🔗 Related Files

- **Backend API**: `../backend/api/views.py`
- **Django Settings**: `../backend/config/settings.py`
- **Main Project README**: `../README.md`

## 👨‍💻 Development Notes

### Code Quality
- Clean, readable code
- Proper error handling
- Console logging for debugging
- Comments explaining logic

### Best Practices Used
- Functional components
- React hooks
- DRY (Don't Repeat Yourself)
- Semantic HTML
- Mobile-first approach

## 📞 Support

For issues or questions:
1. Check the browser console (F12)
2. Verify Django backend is running
3. Check network tab for API responses
4. Review error messages

---

**Last Updated**: February 8, 2026  
**Status**: React Frontend Complete ✅
