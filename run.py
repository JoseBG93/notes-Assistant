#!/usr/bin/env python3
"""
Simple launcher script for Notes Assistant.
Run this file to start the application.
"""

import sys
import os
import traceback  # ← NUEVO: Para mostrar stack trace completo
import logging    # ← NUEVO: Para logging de errores

# NUEVO: Configurar logging básico
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),  # Guarda en archivo
        logging.StreamHandler(sys.stdout)  # Muestra en consola
    ]
)

logger = logging.getLogger(__name__)

# Primary function: Safe application entry point
# Why important: Handles import errors gracefully 
# Add backend/src/ to Python path so we can import modules from that directory
# This allows clean imports like "from main import main" instead of relative paths
# Syntax: 
# sys.path.insert(0, path) - inserts path at index 0 (highest priority). That means that the path will be searched first when importing modules.
# os.path.join() creates platform-independent path. That means that the path will be the same on all operating systems.
# os.path.dirname(__file__) gets current file's directory, which is the directory of the file that is being run.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend/src/'))

def debug_environment():
    """NUEVO: Función para mostrar información del entorno"""
    logger.info("=== DEBUGGING INFORMATION ===")
    logger.info(f"Python version: {sys.version}")
    logger.info(f"Current working directory: {os.getcwd()}")
    logger.info(f"Script location: {__file__}")
    logger.info(f"Python path: {sys.path[:3]}...")  # Primeras 3 rutas
    logger.info("=" * 30)

if __name__ == "__main__": # Main entry point for the application. It is the first file that is run when the application is started.
    try:
        logger.info("🚀 Starting Notes Assistant...")
        debug_environment()  # ← NUEVO: Mostrar info del entorno
        
        logger.info("📦 Importing main module...")
        from main import main # Import the function called "main" from the main.py file, within the src directory.
        
        logger.info("▶️ Running application...")
        main()
        
        logger.info("✅ Application finished successfully")
        
    except ImportError as e:
        logger.error("❌ IMPORT ERROR DETECTED")
        logger.error(f"Error message: {e}")
        logger.error(f"Failed to import from: {os.path.join(os.getcwd(), 'backend/src/')}")
        
        # NUEVO: Mostrar traceback completo
        logger.error("📍 FULL TRACEBACK:")
        logger.error(traceback.format_exc())
        
        # NUEVO: Debugging específico para ImportError
        logger.error("🔍 DEBUGGING SUGGESTIONS:")
        logger.error("1. Check if backend/src/main.py exists")
        logger.error("2. Check if requirements.txt dependencies are installed")
        logger.error("3. Run: pip install -r requirements.txt")
        
        print("\n" + "="*50)
        print("🚨 IMPORT ERROR - Check debug.log for details")
        print("="*50)
        
    except Exception as e:
        logger.error("❌ UNEXPECTED ERROR DETECTED")
        logger.error(f"Error type: {type(e).__name__}")
        logger.error(f"Error message: {e}")
        
        # NUEVO: Mostrar traceback completo
        logger.error("📍 FULL TRACEBACK:")
        logger.error(traceback.format_exc())
        
        # NUEVO: Información adicional para debugging
        logger.error("🔍 DEBUGGING INFO:")
        logger.error(f"Error occurred in: {traceback.extract_tb(e.__traceback__)[-1].filename}")
        logger.error(f"Line number: {traceback.extract_tb(e.__traceback__)[-1].lineno}")
        
        print("\n" + "="*50)
        print("🚨 UNEXPECTED ERROR - Check debug.log for details")
        print("="*50)

