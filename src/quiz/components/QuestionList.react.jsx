import React, {useMemo} from 'react';
import Question from './Question.react';
import {randomizeArray, getStringHash} from '../../service/util/util';
import VerticalLayout from '../../components/core/layout/VerticalLayout.react';
import classes from './style/QuestionList.module.css';

const QuestionList = ({
  questionId,
  questions,
  correct,
  shuffle,
  showFeedback,
  onAnswer,
  multipleCorrect,
  selectedAnswers = [],
}) => {
  const correctAnswers = Array.isArray(correct) ? correct : [correct];
  const correctOptions = correctAnswers.map(i => questions[i]);
  
  let questionsList = useMemo(
    () => (shuffle ? randomizeArray(questions) : [...questions]),
    [shuffle, questions],
  );
  
  const correctIndices = useMemo(
    () => {
      if (shuffle) {
        return correctOptions.map(opt => questionsList.indexOf(opt));
      }
      return correctAnswers;
    },
    [correctOptions, questionsList, correctAnswers, shuffle],
  );

  const questionsComponents = questionsList.map((option, index) => {
    return (
      <Question
        key={getStringHash(`${questionId}_${option}_${index}`)}
        index={index}
        showFeedback={showFeedback}
        questionId={questionId}
        correct={correctIndices}
        onAnswer={onAnswer}
        option={option}
        multipleCorrect={multipleCorrect}
        isSelected={selectedAnswers.includes(index)}
      />
    );
  });
  return (
    <div className={classes.QuestionList}>
      <VerticalLayout>{questionsComponents}</VerticalLayout>
    </div>
  );
};

export default QuestionList;
