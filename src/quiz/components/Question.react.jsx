import React, {useState, useCallback, useMemo, useRef} from 'react';
import classes from './style/Question.module.css';
import {getLetterFromId} from '../../service/util/util';
import Icon from '../../components/core/UI/Icon.react';
import withKeyboardAccessibility from '../../components/hoc/withKeyboardAccessibility.react';

const Question = ({
  index,
  questionId,
  onAnswer,
  showFeedback,
  correct,
  option,
  multipleCorrect,
  isSelected,
}) => {
  const id = `${questionId}_${index}`;
  const [selected, setSelected] = useState(false);
  const questionRef = useRef(null);
  const styles = [classes.Question];
  const correctIndices = Array.isArray(correct) ? correct : [correct];
  const isCorrect = correctIndices.includes(index);
  let iconType;

  if (multipleCorrect) {
    // For multi-select questions
    if (isSelected || selected) {
      styles.push(classes.selected);
    }
    if (showFeedback) {
      styles.push(classes.disabled);
      if (isCorrect) {
        iconType = 'correct';
      } else if (isSelected) {
        iconType = 'incorrect';
      }
    }
  } else {
    // For single-select questions
    if (selected) {
      iconType = isCorrect ? 'correct' : 'incorrect';
      styles.push(classes.selected);
    }

    if (showFeedback) {
      styles.push(classes.disabled);
      if (isCorrect) {
        iconType = 'correct';
      }
    }
  }

  const clickHandler = useCallback(() => {
    if (multipleCorrect) {
      onAnswer(option, isCorrect, index);
    } else {
      setSelected(true);
      onAnswer(option, isCorrect, index);
    }
  }, [isCorrect, option, onAnswer, index, multipleCorrect]);

  const AccessibleLabel = useMemo(
    () => withKeyboardAccessibility(props => <label {...props} />, questionRef),
    [questionRef],
  );

  return (
    <div className={classes.QuestionContainer}>
      <input
        id={id}
        className={classes.hidden}
        type={multipleCorrect ? "checkbox" : "radio"}
        name={questionId}
        onClick={clickHandler}
        value={option}
        disabled={showFeedback}
        ref={questionRef}
        checked={multipleCorrect ? isSelected : selected}
        onChange={() => {}}
      />
      <div>
        <Icon size={1.5} type={iconType} />
      </div>
      <AccessibleLabel className={styles.join(' ')} htmlFor={id}>
        {`${getLetterFromId(index)}) ${option}`}
      </AccessibleLabel>
    </div>
  );
};

export default Question;
