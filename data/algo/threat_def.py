class ThreatAssessment:
    def __init__(self):
        # Define weights for each component - These are maleable
        self.weights = {
            "IOC": 2,
            "TTP": 3,
            "ThreatActor": 4,
            "AffectedAssets": 2,
            "IncidentImpact": 5
        }

        # Define thresholds for classification
        self.thresholds = {
            "No Threat": 5,
            "Possible Threat": 10
        }

    def assess_threat(self, components):
        # Calculate the total score based on the presence of each component
        score = sum(self.weights[component] for component in components if component in self.weights)

        # Determine the threat classification based on the score
        if score <= self.thresholds["No Threat"]:
            return "No Threat"
        elif score <= self.thresholds["Possible Threat"]:
            return "Possible Threat"
        else:
            return "Definite Threat"


threat_assessment = ThreatAssessment()


components_detected = ["IOC", "TTP", "ThreatActor"]

# Assess the threat 
threat_level = threat_assessment.assess_threat(components_detected)
print(f"Threat Level: {threat_level}")

# Example components indicating no threat
components_detected_no_threat = ["IOC"]
threat_level_no_threat = threat_assessment.assess_threat(components_detected_no_threat)
print(f"Threat Level: {threat_level_no_threat}")

# Example components indicating a definite threat
components_detected_definite_threat = ["IOC", "TTP", "ThreatActor", "IncidentImpact"]
threat_level_definite_threat = threat_assessment.assess_threat(components_detected_definite_threat)
print(f"Threat Level: {threat_level_definite_threat}")
