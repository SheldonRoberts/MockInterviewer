environment:
	@echo "Creating the environment..."
	conda env create -f environment.yaml
	@echo "Environment created successfully!"

run-dashboard:
	@echo "Running the dashboard..."
	streamlit run dashboard/main.py