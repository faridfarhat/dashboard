# 🚀 Deployment Guide: GitHub to Render

This guide will help you deploy the AdventureWorks Sales Analytics Dashboard to Render using GitHub.

## Prerequisites

- GitHub account (free at https://github.com)
- Render account (free at https://render.com)
- Git installed on your computer
- All dashboard files ready to commit

## Step 1: Initialize Git Repository Locally

Navigate to your dashboard directory and initialize Git:

```bash
cd /Users/farid/Documents/data_analytics/dashboard/dashboard
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

## Step 2: Add and Commit Files

Stage all files for commit:

```bash
git add .
```

Verify what will be committed:

```bash
git status
```

You should see the following files (and not the `__pycache__` or `.git`):
- `app.py`
- `data.py`
- `requirements.txt`
- `Procfile`
- `.gitignore`
- `README_FULL.md`
- `AdventureWorks Sales Data 2021.csv`
- `AdventureWorks Territory Lookup.csv`
- `pages/overview.py`
- `pages/aggregation.py`
- `pages/distribution.py`
- `pages/__init__.py`

Commit with a descriptive message:

```bash
git commit -m "Initial commit: AdventureWorks Sales Analytics Dashboard"
```

## Step 3: Create GitHub Repository

1. Go to https://github.com/new
2. Enter repository name: `sales-analytics-dashboard`
3. Add description: "Interactive sales analytics dashboard with Dash and Plotly"
4. Choose public or private (public is good for portfolio)
5. Click "Create repository"

## Step 4: Push to GitHub

Follow the instructions on GitHub's new repository page:

```bash
git remote add origin https://github.com/YOUR_USERNAME/sales-analytics-dashboard.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

**Expected output**:
```
Enumerating objects: ...
Counting objects: ...
Compressing objects: ...
Writing objects: ...
Creating new remote tracking branch origin/main
```

## Step 5: Deploy on Render

### 5.1 Create Render Account
- Visit https://render.com
- Sign up with GitHub (recommended for seamless integration)
- Authorize Render to access your GitHub account

### 5.2 Create Web Service

1. Click the "New +" button in Render dashboard
2. Select "Web Service"
3. Click "Connect account" if prompted to connect GitHub
4. Find and select your `sales-analytics-dashboard` repository
5. Click "Connect"

### 5.3 Configure Service

Fill in the following settings:

| Setting | Value |
|---------|-------|
| **Name** | sales-analytics-dashboard |
| **Environment** | Python 3 |
| **Region** | Choose closest to your location (e.g., us-oregon) |
| **Branch** | main |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:server` |
| **Instance Type** | Free (for testing) or Starter+ (recommended) |

### 5.4 Deploy

1. Click "Create Web Service"
2. Render will show you the build logs in real-time
3. Wait for "Your service is live!" message
4. Your dashboard URL will be something like: `https://sales-analytics-dashboard.onrender.com`

## Step 6: Verify Deployment

1. Visit your Render URL
2. You should see the dashboard with the Overview tab selected
3. Test the following:
   - Navigate between Overview, Aggregation, and Distribution tabs
   - Try different grouping options in Aggregation
   - Select different metrics
   - Filter by region

## Troubleshooting Render Deployment

### Build Failed
**Issue**: Build command failed during `pip install`

**Solutions**:
- Check that `requirements.txt` has correct syntax
- Ensure all package versions are compatible
- Try removing version specifiers: `pip install dash plotly pandas numpy gunicorn`

### Service Not Starting
**Issue**: Build succeeds but service won't start

**Solutions**:
- Check logs: Look at Render dashboard logs for errors
- Verify `Procfile`: Should contain `web: gunicorn app:server`
- Check `app.py`: Ensure `server = app.server` is present

### Data Files Not Found
**Issue**: Application starts but shows errors about CSV files

**Solutions**:
- Verify CSV files are committed to GitHub:
  ```bash
  git ls-files | grep csv
  ```
- Check file permissions in Render logs
- Ensure CSV files are in the root directory with `app.py`

### Dashboard Loads but Charts Don't Show
**Issue**: Pages load but visualizations are blank

**Solutions**:
- Check browser console (F12) for JavaScript errors
- Verify data.py loads files correctly
- Check Render logs for Python errors
- Try restarting the service (use Render dashboard)

## Updating Your Dashboard

After making changes locally:

```bash
# Make changes to your files
# Test locally: python app.py

# Stage and commit
git add .
git commit -m "Update: describe your changes"

# Push to GitHub
git push origin main
```

Render will automatically detect the push and redeploy your application (usually within 1 minute).

## Monitoring Your Application

### View Logs
1. Go to your service in Render dashboard
2. Click "Logs" tab
3. View real-time logs and error messages

### Check Service Status
1. Go to service dashboard
2. See CPU, memory, and request metrics
3. Monitor performance

### Scale Service
- Free tier: 0.5 CPU, 512 MB RAM
- Starter: 0.5 CPU, 1 GB RAM (recommended)
- Higher tiers available for production

## Cost Considerations

**Render Free Tier**:
- Spins down after 15 minutes of inactivity
- May have cold start delays
- Perfect for demos and testing

**Starter Plan ($7/month)**:
- Always running
- No cold starts
- Recommended for personal projects
- Includes custom domains

## Next Steps

1. ✅ Deploy your dashboard
2. Share the URL with others
3. Monitor the logs for issues
4. Consider upgrading to Starter plan for better performance
5. Add more features and redeploy

## Tips for Success

- **Keep requirements.txt updated**: After installing new packages, run `pip freeze > requirements.txt`
- **Test locally first**: Always test changes with `python app.py` before pushing
- **Monitor cold starts**: On free tier, first request after 15 minutes may be slow
- **Check logs regularly**: Render logs show errors you might miss locally
- **Use meaningful commit messages**: Makes it easier to track changes
- **Set up GitHub notifications**: Know when deployment succeeds/fails

## Security Notes

- Keep sensitive data (API keys, passwords) out of code
- Use environment variables for configuration
- Don't commit secrets to GitHub
- Use `.gitignore` to exclude sensitive files

## Additional Resources

- [Render Documentation](https://render.com/docs)
- [Dash Deployment Guide](https://dash.plotly.com/deployment)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [GitHub Guides](https://guides.github.com)

---

**Questions?** Check the dashboard's GitHub issues or Render support.

Good luck! 🎉
