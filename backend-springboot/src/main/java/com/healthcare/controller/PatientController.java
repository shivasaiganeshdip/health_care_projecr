package com.healthcare.controller;

import com.healthcare.entity.Patient;
import com.healthcare.service.PatientService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/patients")
@CrossOrigin
public class PatientController {

    @Autowired
    private PatientService service;

    @PostMapping
    public Patient savePatient(@RequestBody Patient patient) {
        return service.savePatient(patient);
    }

    @GetMapping
    public List<Patient> getPatients() {
        return service.getAllPatients();
    }
}
