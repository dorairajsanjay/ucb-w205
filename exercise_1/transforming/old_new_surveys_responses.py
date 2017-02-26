from pyspark import HiveContext
from pyspark import SparkContext
from pyspark.sql.types import IntegerType

sc=SparkContext()

rdd=HiveContext(sc).sql('select provider_number as provider_id,communication_with_nurses_achievement_points,communication_with_nurses_improvement_points,communication_with_nurses_dimension_score,communication_with_doctors_achievement_points,communication_with_doctors_improvement_points,communication_with_doctors_dimension_score,responsiveness_of_hospital_staff_achievement_points,responsiveness_of_hospital_staff_improvement_points,responsiveness_of_hospital_staff_dimension_score,pain_management_achievement_points,pain_management_improvement_points,pain_management_dimension_score,communication_about_medicines_achievement_points,communication_about_medicines_improvement_points,communication_about_medicines_dimension_score,cleanliness_and_quietness_of_hospital_environment_achievement_points,cleanliness_and_quietness_of_hospital_environment_improvement_points,cleanliness_and_quietness_of_hospital_environment_dimension_score,discharge_information_achievement_points,discharge_information_improvement_points,discharge_information_dimension_score,overall_rating_of_hospital_achievement_points,overall_rating_of_hospital_improvement_points,overall_rating_of_hospital_dimension_score,hcahps_base_score,hcahps_consistency_score from surveys_responses')
 
from pyspark.sql.functions import udf

#create a normalizer method for normalizing all survey surveys to a 0 to 10 scale
#normalize_response = udf(lambda response: int(float(response.split()[0])/float(response.split()[3])*10), IntegerType())
normalize_response = udf(lambda response: int(float(response.split()[0])/float(response.split()[3])*10) if response != "Not Available" else int(-1), IntegerType())
integer_check = udf(lambda response: int(response) if response != "Not Available" else int(-1),IntegerType())

rdd = rdd.withColumn("communication_with_nurses_achievement_points",normalize_response(rdd.communication_with_nurses_achievement_points))
#rdd.select('communication_with_nurses_achievement_points').take(10)

rdd = rdd.withColumn("communication_with_nurses_improvement_points",normalize_response(rdd.communication_with_nurses_improvement_points))
#rdd.select('communication_with_nurses_improvement_points').take(10)

rdd = rdd.withColumn("communication_with_nurses_dimension_score",normalize_response(rdd.communication_with_nurses_dimension_score))
#rdd.select('communication_with_nurses_dimension_score').take(10)
rdd = rdd.withColumn("communication_with_doctors_achievement_points",normalize_response(rdd.communication_with_doctors_achievement_points))
#rdd.select('communication_with_doctors_achievement_points').take(10)
rdd = rdd.withColumn("communication_with_doctors_improvement_points",normalize_response(rdd.communication_with_doctors_improvement_points))
#rdd.select('communication_with_doctors_improvement_points').take(10)
rdd = rdd.withColumn("communication_with_doctors_dimension_score",normalize_response(rdd.communication_with_doctors_dimension_score))
#rdd.select('communication_with_doctors_dimension_score').take(10)
rdd = rdd.withColumn("responsiveness_of_hospital_staff_achievement_points",normalize_response(rdd.responsiveness_of_hospital_staff_achievement_points))
#rdd.select('responsiveness_of_hospital_staff_achievement_points').take(10)
rdd = rdd.withColumn("responsiveness_of_hospital_staff_improvement_points",normalize_response(rdd.responsiveness_of_hospital_staff_improvement_points))
#rdd.select('responsiveness_of_hospital_staff_improvement_points').take(10)
rdd = rdd.withColumn("responsiveness_of_hospital_staff_dimension_score",normalize_response(rdd.responsiveness_of_hospital_staff_dimension_score))
#rdd.select('responsiveness_of_hospital_staff_dimension_score').take(10)
rdd = rdd.withColumn("pain_management_achievement_points",normalize_response(rdd.pain_management_achievement_points))
#rdd.select('pain_management_achievement_points').take(10)
rdd = rdd.withColumn("pain_management_improvement_points",normalize_response(rdd.pain_management_improvement_points))
#rdd.select('pain_management_improvement_points').take(10)
rdd = rdd.withColumn("pain_management_dimension_score",normalize_response(rdd.pain_management_dimension_score))
#rdd.select('pain_management_dimension_score').take(10)
rdd = rdd.withColumn("communication_about_medicines_achievement_points",normalize_response(rdd.communication_about_medicines_achievement_points))
#rdd.select('communication_about_medicines_achievement_points').take(10)
rdd = rdd.withColumn("communication_about_medicines_improvement_points",normalize_response(rdd.communication_about_medicines_improvement_points))
#rdd.select('communication_about_medicines_improvement_points').take(10)
rdd = rdd.withColumn("communication_about_medicines_dimension_score",normalize_response(rdd.communication_about_medicines_dimension_score))
#rdd.select('communication_about_medicines_dimension_score').take(10)
rdd = rdd.withColumn("cleanliness_and_quietness_of_hospital_environment_achievement_points",normalize_response(rdd.cleanliness_and_quietness_of_hospital_environment_achievement_points))
#rdd.select('cleanliness_and_quietness_of_hospital_environment_achievement_points').take(10)
rdd = rdd.withColumn("cleanliness_and_quietness_of_hospital_environment_improvement_points",normalize_response(rdd.cleanliness_and_quietness_of_hospital_environment_improvement_points))
#rdd.select('cleanliness_and_quietness_of_hospital_environment_improvement_points').take(10)
rdd = rdd.withColumn("cleanliness_and_quietness_of_hospital_environment_dimension_score",normalize_response(rdd.cleanliness_and_quietness_of_hospital_environment_dimension_score))
#rdd.select('cleanliness_and_quietness_of_hospital_environment_dimension_score').take(10)
rdd = rdd.withColumn("discharge_information_achievement_points",normalize_response(rdd.discharge_information_achievement_points))
#rdd.select('discharge_information_achievement_points').take(10)
rdd = rdd.withColumn("discharge_information_improvement_points",normalize_response(rdd.discharge_information_improvement_points))
#rdd.select('discharge_information_improvement_points').take(10)
rdd = rdd.withColumn("discharge_information_dimension_score",normalize_response(rdd.discharge_information_dimension_score))
#rdd.select('discharge_information_dimension_score').take(10)
rdd = rdd.withColumn("overall_rating_of_hospital_achievement_points",normalize_response(rdd.overall_rating_of_hospital_achievement_points))
#rdd.select('overall_rating_of_hospital_achievement_points').take(10)
rdd = rdd.withColumn("overall_rating_of_hospital_improvement_points",normalize_response(rdd.overall_rating_of_hospital_improvement_points))
#rdd.select('overall_rating_of_hospital_improvement_points').take(10)
rdd = rdd.withColumn("overall_rating_of_hospital_dimension_score",normalize_response(rdd.overall_rating_of_hospital_dimension_score))
#rdd.select('overall_rating_of_hospital_dimension_score').take(10)
#rdd = rdd.withColumn("hcahps_base_score",rdd["hcahps_base_score"].cast(IntegerType()))
rdd = rdd.withColumn("hcahps_base_score",integer_check(rdd.hcahps_base_score))
rdd = rdd.withColumn("hcahps_consistency_score",integer_check(rdd.hcahps_consistency_score))

#rdd.select('hcahps_base_score').take(10)
#rdd = rdd.withColumn("hcahps_consistency_score",rdd["hcahps_consistency_score"].cast(IntegerType()))
#rdd.select('hcahps_consistency_score').take(10)

#rdd.write.mode('overwrite').saveAsTable("new2_surveys_responses")
#rdd.write.mode('overwrite').saveAsTable("new2_surveys_responses")
rdd.rdd.saveAsTextFile('/user/w205/hospital_compare/new_surveys_responses')